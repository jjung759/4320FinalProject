<?php
  class LoginModel {
    private $error = '';
    private $mysqli;
    private $user;

    public function __construct() {
      session_start();
      $this->initDatabaseConnection();
    }

    public function __destruct() {
      if ($this->mysqli) {
        $this->mysqli->close();
      }
    }

    public function getError() {
      return $this->error;
    }

    private function initDatabaseConnection() {
      require('db_connection.php');
      $this->mysqli = new mysqli($servername, $username, $password, $dbname);
      if ($this->mysqli->connect_error) {
        $this->error = $mysqli->connect_error;
      }
    }

    public function addAccount($data) {
			$this->error = '';

      $firstname = $data['firstname'];
      $middlename = ($data['middlename']) ? $data['middlename'] : '';
      $lastname = $data['lastname'];
      $email = $data['email'];
      $username = $data['username'];
      $password = $data['password'];

      // Error Checking for Database
			if (!$firstname) {
				$this->error = "No first name found. A first name is required.";
				return $this->error;
			}
      if (!$lastname) {
        $this->error = "No last name found. A last name is required.";
        return $this->error;
      }
      if (!$email) {
        $this->error = "No email address found. An email is required.";
        return $this->error;
      }
      if (!$username) {
        $this->error = "No username found. A username is required.";
        return $this->error;
      }
      if (!$password) {
        $this->error = "No password found. A password is required.";
        return $this->error;
      }

      $firstnameEscaped = $this->mysqli->real_escape_string($firstname);
 			$middlenameEscaped = $this->mysqli->real_escape_string($middlename);
 			$lastnameEscaped = $this->mysqli->real_escape_string($lastname);
      $emailEscaped = $this->mysqli->real_escape_string($email);
      $usernameEscaped = $this->mysqli->real_escape_string($username);
      $passwordEscaped = $this->mysqli->real_escape_string($password);
      $passwordHashed = $this->mysqli->password_hash($passwordEscaped);

			$sql = "INSERT INTO Client (firstname, middlename, lastname, nickname, gender, ssn, birthDate) VALUES ('$firstnameEscaped', '$middlenameEscaped', '$lastnameEscaped', '$emailEscaped', '$usernameEscaped', '$passwordHashed')";

			if (! $result = $this->mysqli->query($sql)) {
				$this->error = $this->mysqli->error;
			}

    	return $this->error;
    }
  }
?>
