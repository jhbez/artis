# -*- coding: utf-8 -*-

#   Copyright 2019, Joinher
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from flask import current_app

def inject_env():

    return dict(
        title = current_app.config.get("TITLE","Blak Artis"),
        theme = current_app.config.get("THEME", "blakartis"),
        
        # Social Media
        facebook = current_app.config.get("FACEBOOK", 'https://www.facebook.com/blakartis'),
        px500 = current_app.config.get("PX500", 'https://www.500px.com/blakartis'),
        instagram = current_app.config.get("INSTAGRAM", 'https://www.instagram.com/blakartis/'),
        joinher = current_app.config.get("JOINHER", 'https://www.joinher.com/blakartis/'),
    )