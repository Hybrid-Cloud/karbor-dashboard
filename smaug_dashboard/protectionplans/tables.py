#    Copyright (c) 2016 Huawei, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from horizon import tables

from smaug_dashboard.api import smaug as smaugclient


class DeleteProtectionPlansAction(tables.DeleteAction):
    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Delete Protection Plan",
            u"Delete Protection Plans",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Delete Protection Plan",
            u"Delete Protection Plans",
            count
        )

    def allowed(self, request, protectionplan):
        return True

    def delete(self, request, obj_id):
        smaugclient.plan_delete(request, obj_id)


class ProtectionPlanFilterAction(tables.FilterAction):
    def filter(self, table, protectionplans, filter_string):
        """Naive case-insensitive search."""
        query = filter_string.lower()
        return [protectionplan for protectionplan in protectionplans
                if query in protectionplan.name.lower()]


class ProtectionPlansTable(tables.DataTable):
    name = tables.Column('name',
                         verbose_name=_('Name'))

    status = tables.Column('status',
                           verbose_name=_('Status'))

    class Meta(object):
        name = 'protectionplans'
        verbose_name = _('Protection Plans')
        row_actions = (DeleteProtectionPlansAction,)
        table_actions = (ProtectionPlanFilterAction,
                         DeleteProtectionPlansAction)