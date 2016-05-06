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


class DeleteCheckpointsAction(tables.DeleteAction):
    @staticmethod
    def action_present(count):
        return ungettext_lazy(u"Delete Checkpoint",
                              u"Delete Checkpoints",
                              count)

    @staticmethod
    def action_past(count):
        return ungettext_lazy(u"Deleted Checkpoint",
                              u"Deleted Checkpoints",
                              count)

    def allowed(self, request, checkpoint):
        return True

    def delete(self, request, obj_id):
        datum = self.table.get_object_by_id(obj_id)
        provider_id = datum.provider_id
        smaugclient.checkpoint_delete(request,
                                      provider_id=provider_id,
                                      checkpoint_id=obj_id)


def get_plan_name(obj):
    name = ""
    plan = getattr(obj, 'protection_plan')
    if plan is not None:
        name = plan.get("name")
    return name


class CheckpointsTable(tables.DataTable):
    checkpointId = tables.Column(
        "id",
        verbose_name=_('Checkpoint ID'))
    protectionProvider = tables.Column(
        "provider_name",
        verbose_name=_('Protection Provider'))
    protectPlan = tables.Column(
        get_plan_name,
        verbose_name=_('Protection Plan'))
    status = tables.Column(
        'status',
        verbose_name=_('Status'))

    class Meta(object):
        name = 'checkpoints'
        verbose_name = _('Checkpoints')
        row_actions = (DeleteCheckpointsAction,)