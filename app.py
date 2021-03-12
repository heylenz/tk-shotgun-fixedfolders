# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
App that creates folders on disk from inside of Shotgun.

"""
import sgtk
from tank.platform import Application
import tank




class FixedFolders(Application):
    def init_app(self):

        deny_permissions = self.get_setting("deny_permissions")
        deny_platforms = self.get_setting("deny_platforms")

        p = {
            "title": "Fixed Folders",
            "deny_permissions": deny_permissions,
            "deny_platforms": deny_platforms,
            "supports_multiple_selection": True,
        }

        self.engine.register_command("fixed_folders", self.fixed_folders, p)


    def fixed_folders(self, entity_type, entity_ids):
        if len(entity_ids) == 0:
            self.log_info("No entities specified!")
            return

        tk = self.engine.sgtk
        unreg_cmd = sgtk.get_command('unregister_folders', tk)

        for entity_id in entity_ids:
            parameters = {"entity": {'type':entity_type, 'id': entity_id}}
            unreg_cmd.execute(parameters)
