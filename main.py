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
    <form action: '/' method:'post'>
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
class MainHandler(webapp2.RequestHandler):
    def write_page(self, name, name_error, password="", pw_error, verify_pw = "", vpw_error, email):
        #construct page
        page = page_header + signup_form + page_footer
        self.response.write(page % {"name":name, "name":name_error, "email":email, "password":pw_error, "verify_pw":vpw_error})  
        
    def get(self):
        #render page
        self.write_page(self, name = "", name_error = "", password="", pw_error = "", verify_pw = "", vpw_error = "", email="")
        
    def post(self):
        #get user's input
        #error = False
        u_name = cgi.escape(self.request.get('name'))
        u_password = cgi.escape(self.request.get('password'))
        u_verify_pw = cgi.escape(self.request.get('verify_pw'))
        email = cgi.escape(self.request.get('email'))
        
        def valid_name(self, n):
        #validate user's input & provide error msg if input does not validate
            if (not n) or (n.strip() == ""):
                name_error = "Please set your password."
                self.response.write_page(self, name, name_error, password="", pw_error, verify_pw = "", vpw_error, email)
                #self.redirect("/?error" + cgi.escape(error, quote=True))
            else:
                return n
                
        def valid_password(self, pw):
            if (not pw) or (pw.strip() == ""):
                pw_error = "Please verify your password."
                self.response.write_page(self, name, name_error, password="", pw_error, verify_pw = "", vpw_error, email)
                #self.redirect("/?error" + cgi.escape(error, quote=True))
            else:
                return pw
                
        def valid_verify_pw(self, verify_pw):                
            if (not verify_pw) or (verify_pw.strip() == ""):
                vpw_error = "Please verify your password."
                self.response.write_page(vpw_error, quote=True)
                #self.redirect("/?error" + cgi.escape(error, quote=True))
            elif not (password == verify_pw):
                vpw_error = "Your passwords do not match." 
                self.response.write_page(self, name, name_error, password="", pw_error, verify_pw = "", vpw_error, email)
                #self.redirect("/?error" + cgi.escape(error, quote=True))
            else:
                return verify_pw 
                
        #validate user input
        name = valid_name(u_name)
        password = valid_password(u_password)
        verify_pw = valid_verify_pw('u_verify_pw')      
        
        if not name and not password and not verify_pw:
            self.response.write_page()
        else:
            self.redirect('/welcome')    
                
class Welcome(webapp2.RequestHandler):
    def get(self):
    #if validated Welcome the new User
        name = cgi.escape(self.request.get('name'))
        welcome = page_header + "<h3>Welcome, " + name + "</h3>"+ page_footer
        self.response.write(welcome)
        
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/welcome", Welcome)
], debug=True)
