/*  Copyright (c) 2016 Huawei, Inc.

    Licensed under the Apache License, Version 2.0 (the "License"); you may
    not use this file except in compliance with the License. You may obtain
    a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    License for the specific language governing permissions and limitations
    under the License.
*/

/* set the choose resources */
function setRestoredResource() {
  var trResources = $("#checkpointRestoreResource tr[resource-id]");
  var provider = $.parseJSON($(".provider").val());
  var parameters = $.Karbor.getResourceDefaultParameters(provider, "restore_schema");
  if(trResources != null) {
    trResources.each(function() {
      var trResource = $(this);
      var resourceid = trResource.attr("resource-id");
      var parameterbtn = trResource.find(".editparameters");
      var resourcetype =parameterbtn.attr("resourcetype");
      var userdata = parameterbtn.data("userdata");
      if(userdata!=null) {
        parameters[resourcetype + "#" + resourceid] = userdata;
      }
    });
  }
  $(".parameters").val(angular.toJson(parameters));
}

horizon.checkpoints_restore = {
  /* init create plan dialog */
  init: function(){
   /* init resource tree */
    $("#checkpointRestoreResource").treetable({ expandable: true });

    /* init protection provider */
    (function() {
      var provider = $.parseJSON($(".provider").val());
      if(provider != null) {
        if(provider.extended_info_schema != null) {
          var result = provider.extended_info_schema['restore_schema'];
          for(var r in result) {
            $("#checkpointRestoreResource").find("input[resourcetype='" + r + "']").data("schema", result[r]);
            $("#checkpointRestoreResource").find("input[resourcetype='" + r + "']").data("userdata", null);
          }
        }
      }
    })();

    /* bind create button event */
    $(".btn-primary").bind("click", function() {
      setRestoredResource();
      return true;
    });

    /* live resource parameters event */
    $(document).on('click', ".editparameters", function(){
      var schema = $(this).data("schema");
      var userdata = $(this).data("userdata");
      var resourceid = $(this).closest("tr").attr("resource-id");
      if(schema != null) {
        var exist_ui_dialogs = $("body").has(".ui-dialog");
        if(exist_ui_dialogs.length == 0){
          var dialog_data = $.Karbor.createDialog(schema, userdata, resourceid);
          $.Karbor.openDialog(dialog_data, "#parametersdialog", "div.dialog_wrapper");
        }
      }
    });

    /* bind parameters dialog save button event */
    $(document).on('click', "#parametersdialog .btn.btn-primary", function() {
      var flag = $.Karbor.check_required($("#parametersdialog"));
      if(flag) {
        var resourceid = $("#parametersdialog .modal-body").attr("resourceid");
        var form_controls = $("#parametersdialog .modal-body .form-control");
        var userdata = $.Karbor.getDynamicValue(form_controls);
        $("#checkpointRestoreResource").find("tr[resource-id='" + resourceid + "']")
                                       .find(".editparameters")
                                       .data("userdata", userdata);
        $.Karbor.closeDialog("#parametersdialog");
      }
    });

    /* bind parameters dialog cancel button event */
    $(document).on('click', "#parametersdialog .btn.cancel", function() {
      $.Karbor.closeDialog("#parametersdialog");
    });

    /* bind parameters dialog close button event */
    $(document).on('click', "#parametersdialog a.close", function() {
      $.Karbor.closeDialog("#parametersdialog");
    });
  }
};
