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

    //Establish connection to the database. Using the required document to store database info (Servername, username, password, database name)
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
      $middlename = ($data['middlename']) ? $data['middlename'] : ''; //Middlename is optional
      $lastname = $data['lastname'];
      $email = $data['email'];
      $username = $data['username'];
      $password = $data['password'];
      $confirm_password = $data['confirm_password'];

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

      if($password != $confirm_password){
        $this->error= "The passwords do not match.";
        return $this->error;
      }

      //Escaped values for database insert
      $firstname_escaped = $this->mysqli->real_escape_string($firstname);
 			$middlename_escaped = $this->mysqli->real_escape_string($middlename);
 			$lastname_escaped = $this->mysqli->real_escape_string($lastname);
      $email_escaped = $this->mysqli->real_escape_string($email);
      $username_escaped = $this->mysqli->real_escape_string($username);
      $password_escaped = $this->mysqli->real_escape_string($password);
      $password_hashed = password_hash($password_escaped, PASSWORD_BCRYPT);

      //Inserts new account into the database, with hashed password
			$sql = "INSERT INTO Customer (firstname, middlename, lastname, email, username, passwordHash) VALUES ('$firstname_escaped', '$middlename_escaped', '$lastname_escaped', '$email_escaped', '$username_escaped', '$password_hashed')";

			if (! $result = $this->mysqli->query($sql)) {
				$this->error = $this->mysqli->error;
			}

    	return $this->error;
    }

    //Not yet funcitonal
    public function login($data){
      $this->error = '';

      $username = $data['username'];
      $password = $data['password'];

      if (!$username) {
        $this->error = "No username found. A username is required.";
        return $this->error;
      }
      if (!$password) {
        $this->error = "No password found. A password is required.";
        return $this->error;
      }

      $username_escaped = $this->mysqli->real_escape_string($username);
      $password_escaped = $this->mysqli->real_escape_string($username);
      // $password_verify = password_verify($password_escaped, $password_hashed);
      $sql = "SELECT name, email FROM Customer WHERE username='$username' AND password='$password_escaped'";
      if (! $result = $this->mysqli->query($sql)) {
				$this->error = $this->mysqli->error;
			}
      else print "Login successful.";
    }
  }
?>
