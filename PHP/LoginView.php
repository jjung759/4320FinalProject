<?php

  class LoginViews {
    private $stylesheet = 'LoginForm.css';
		private $page_title = 'News Aggregator Login';

    public function __construct() {

    }

    public function __destruct() {

    }

    public function loginView($data = null, $message = '') {
      $username = '';
      $password = '';

      if ($data) {
        $username = $data['username'];
        $password = $data['password'];
      }

      if ($message) {
				$body .= "<p class='message'>$message</p>\n";
			}

      $body = "<h1>Login</h1>";
      $body .= "<form action='index.php' method = 'post'>";
      $body .= "<input type='hidden' name='action' value='login' />";
      $body .= <<<EOT
        <p>Username<br /><input type='text' name='username' value='$username' placeholder='Enter Username' maxlength='255' size='40' required></p>
        <p>Password<br /><input type='password' name='password' value='$password' placeholder='Enter Password' maxlength='255' size='40' required></p>
        <input type='submit' value='Login'></form>
        <form><p style='font-size: 12px'>New to our site?
        <a class='buttons' href='index.php?view=addAccount'>Create Account</a></p></form>\n
EOT;
      return $this->page($body);
    }

    public function addAccountForm($data = null, $message = '') {
      $firstname = '';
      $middlename = '';
      $lastname = '';
      $email= '';
      $username = '';
      $password = '';
      $confirm_password = '';

      if ($data) {
        $firstname = $data['firstname'];
        $middlename = $data['middlename'] ? $data['middlename'] : '';
        $lastname = $data['lastname'];
        $email = $data['email'];
        $username= $data['username'];
        $password = $data['password'];
        $confirm_password = $data['confirm_password'];
      }

      if ($message) {
        $body .= "<p class='message'>$message</p>\n";
      }

      $body = "<h1>Create an Account</h1>";
      $body .= "<form action='index.php' method='post'>";
      $body .= "<input type='hidden' name='action' value='addAccount' />";

      $body .= <<<EOT
        <p>First Name<br />
        <input type="text" name="firstname" value="$firstname" placeholder="Enter your first name" maxlength="255" size="40" required></p>
        <p>Middle Name<br />
        <input type="text" name="middlename" value = "$middlename" placeholder="Enter your middle name or initial" maxlength="255" size="40"></p>
        <p>Last Name<br />
        <input type="text" name="lastname" value="$lastname" placeholder="Enter your last name" maxlength="255" size="40" required></p>
        <p>Email<br />
        <input type="text" name="email" value="$email" placeholder="Enter your email address" maxlength="255" size="40" required></p>
        <p>Username<br />
        <input type="text" name="username" value="$username" placeholder="Enter Username" maxlength="255" size="40" required></p>
        <p>Password<br />
        <input type="password" name="password" value="$password" placeholder="Enter Password" maxlength="255" size="40" required></p>
        <p>Confirm Password<br />
        <input type="password" name="confirm_password" value="$confirm_password" placeholder="Confirm Password" maxlength="255" size="40" required></p>
        <input type="submit" name='submit' value="Submit"> <input type="reset" name='reset' value="Reset">
        </form>
        <form><p style='font-size:12px'>Already have an account?<a class='buttons' href='index.php?view=loginView'>Sign in</a></p></form>
        </body>
        </html>
EOT;

    return $this->page($body);
    }

    public function errorView($message) {
      $body = "<h1>Login</h1>\n";
      $body .= "<p>$message</p>\n";

      return $this->page($body);
    }

    private function page($body) {
      $html = <<<EOT
        <!DOCTYPE html>
        <html>
        <head>
        <title>{$this->page_title}</title>
        <link rel="stylesheet" type="text/css" href="{$this->stylesheet}">
        </head>
        <body>
        $body
        </body>
        </html>
EOT;
      return $html;
    }
  }
?>
