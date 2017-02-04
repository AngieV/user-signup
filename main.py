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
    <h2>User Signup</h2>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

#define form 
signup_form = """
    <form method='post'>
        <table>
            <tr><td class='label'>Name: </td>
                <td><input type = 'text' name ='name' value="%(name)s"></td><td class='error'>%(name_error)s</td></tr>
            <tr><td class='label'>Password: </td> 
                <td><input type = 'password' name ='password' value = ''></td><td class='error'>%(pw_error)s</td></tr>
            <tr><td class='label'>Verify password: </td>
                <td><input type = 'password' name ='verify_pw' value = ''></td><td class='error'>%(vpw_error)s</td></tr>
            <tr><td class='label'>Email: (optional)</td>
                <td><input type = 'text' name ='email' value="%(email)s"></td></tr>
            <tr><td><input type='submit' value ='Submit'></tr>
        </table>
   </form>
    """   
    
#validate user's input & provide error msg if input does not validate

def valid_name(u_name):
    if (not u_name) or (u_name.strip() == ""):
        return False
    return True    
                
def valid_password(u_password):
    if (not u_password) or (u_password.strip() == ""):
        return False
    return True   
                
def valid_verify_pw(u_password, u_verify_pw):                
    if not u_verify_pw or (u_verify_pw.strip() == ""):
        return False
    if not (u_password == u_verify_pw):
        return False
    return True
                                                                                                                              
class MainHandler(webapp2.RequestHandler):
    def write_page(self, name="", name_error="", pw_error = "", vpw_error = "", email=""):
        #construct page
        page = page_header + signup_form + page_footer
        self.response.write(page % {"name":name, "name_error":name_error, "email":email, "pw_error":pw_error, "vpw_error":vpw_error})  
        
    def get(self):
        #render page
        self.write_page()
        
    def post(self):
    #get user's input
        u_name = cgi.escape(self.request.get('name'))
        u_password = cgi.escape(self.request.get('password'))
        u_verify_pw = cgi.escape(self.request.get('verify_pw'))
        email = cgi.escape(self.request.get('email'))
                
        #validate user input 
        name = valid_name(u_name)
        password = valid_password(u_password)
        verify_pw = valid_verify_pw(u_password, u_verify_pw)      
        
        if (name and password and verify_pw):
            self.redirect('/welcome?u_name='+ u_name)   
        if not name:
            name_error = "Please provide your name."
        else:
            name_error = ""
        if not password:
            pw_error = "Please set your password."
        else:
            pw_error = ""
        if not verify_pw:
            vpw_error = "Please verify your password."
        else: 
            vpw_error = ""
        self.write_page(u_name, name_error, pw_error, vpw_error, email)
            
                
class Welcome(webapp2.RequestHandler):
    def get(self):
    #if validated Welcome the new User
        name = self.request.get('u_name')
        welcome = page_header + "<h3>Welcome, " + name + "</h3>" + page_footer
        self.response.write(welcome)
        
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/welcome", Welcome)
], debug=True)
