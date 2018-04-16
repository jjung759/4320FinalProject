<?php

  class LoginViews {
    private $stylesheet = 'LoginForm.css';
		private $pageTitle = 'News Aggregator Login';

    public function __construct() {

    }

    public function __destruct() {

    }

    public function loginView($message = '') {
      $body = "<h1>Login</h1>";

      if ($message) {
				$body .= "<p class='message'>$message</p>\n";
			}

      $body .= "<p><a class='addAccount' href='index.php?view=addAccount'>+ Create Account</a></p>\n";
      $body .= "<p>Username<br /><input type='text' name='username' value='$username' placeholder='Enter Username' maxlength='255' size='40' required></p>";
      $body .= "<p>Password<br /><input type='password' name='password' value='$password' placeholder='Enter Password' maxlength='255' size='40' required></p>";

      $body .= "<tr>";
      $body .= "<th><form action='index.php' method='post'><input type='hidden' name='action' value='loginView'/>";
      $body .= "</tr>\n";

      return $this->page($body);
    }

    public function addAccountForm($data = null, $message = '') {
      $firstname = '';
      $middlename = '';
      $lastname = '';
      $email= '';
      $username = '';
      $password = '';
      if ($data) {
        $firstname = $data['firstname'];
        $middlename = $data['middlename'] ? $data['middlename'] : '';
        $lastname = $data['lastname'];
        $email = $data['email'];
        $username= $data['username'];
        $password = $data['password'];
      }

      $body = <<<EOT1
    <!DOCTYPE html>
    <html>
    <head>
    <title>News Aggregator</title>
    <link rel="stylesheet" type="text/css" href="$stylesheet" />
    </head>
    <body>
    <h1>Create an Account</h1>
EOT1;

      if ($message) {
        $body .= "<p class='message'>$message</p>\n";
      }

      $body .= "<form action='index.php' method='post'>";

      if ($data['id']) {
        // $body .= "<input type='hidden' name='action' value='updateClient' />";
        // $body .= "<input type='hidden' name='clientId' value='{$data['id']}' />";
      } else {
        $body .= "<input type='hidden' name='action' value='addAccount' />";
      }

      $body .= <<<EOT2
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
    <input type="submit" name='submit' value="Submit"> <input type="submit" name='cancel' value="Cancel">
    </form>
    </body>
    </html>
EOT2;

    return $this->page($body);
    }

    public function errorView($message) {
      $body = "<h1>Clients</h1>\n";
      $body .= "<p>$message</p>\n";

      return $this->page($body);
    }

    private function page($body) {
      $html = <<<EOT
      <!DOCTYPE html>
      <html>
      <head>
      <title>{$this->pageTitle}</title>
      <link rel="stylesheet" type="text/css" href="{$this->stylesheet}">
      </head>
      <body>
      $body
      </body>
      </html>
EOT;
    }
  }
?>
