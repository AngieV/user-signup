#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h2>
        <a href="/">User Signup</a>
    </h2>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

#define form components
name =  "<label>Name: <input type = 'text' name ='name'></label><br/>"
passwd = "<label>Password: <input type = 'password' name ='passwd' ></label><br/>"
verify_pw = "<label>Verify password: <input type = 'password' name ='verify_pw' ></label><br/>"
email = "<label>Email: <input type = 'text' name ='email' ></label><br/>"
submit = "<input type='submit' value ='Submit'>"
#"<div class='error'>%(error)s</div>"
#construct form
form = "<form method:'post' action = '/register' >" + name + passwd + verify_pw + email + submit + "</form>"
#construct page
page = page_header + form + page_footer

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(page)
    

        
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
