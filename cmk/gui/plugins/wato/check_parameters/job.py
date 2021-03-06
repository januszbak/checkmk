#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Age,
    Dictionary,
    DropdownChoice,
    TextAscii,
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)


def _parameter_valuespec_job():
    return Dictionary(elements=[
        ("age",
         Tuple(
             title=_("Maximum time since last start of job execution"),
             elements=[
                 Age(title=_("Warning at"), default_value=0),
                 Age(title=_("Critical at"), default_value=0)
             ],
         )),
        ("outcome_on_cluster",
         DropdownChoice(
             title=_("Clusters: Prefered check result of local checks"),
             help=_("If you're running local checks on clusters via clustered services rule "
                    "you can influence the check result with this rule. You can choose between "
                    "best or worst state. Default setting is worst state."),
             choices=[
                 ("worst", _("Worst state")),
                 ("best", _("Best state")),
             ],
             default_value="worst")),
    ],)


rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="job",
        group=RulespecGroupCheckParametersApplications,
        item_spec=lambda: TextAscii(title=_("Job name"),),
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_job,
        title=lambda: _("Age of jobs controlled by mk-job"),
    ))
