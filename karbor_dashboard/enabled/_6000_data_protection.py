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


# The name of the dashboard to be added to HORIZON['dashboards']. Required.
DASHBOARD = 'karbor'

# If set to True, this dashboard will not be added to the settings.
DISABLED = False

ADD_INSTALLED_APPS = [
    'karbor_dashboard',
]

# Automatically discover static resources in installed apps
AUTO_DISCOVER_STATIC_FILES = True
