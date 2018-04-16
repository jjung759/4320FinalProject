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
      $confirmPassword = $data['confirmPassword'];

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

      if($password != $confirmPassword){
        $this->error= "The passwords do not match.";
        return $this->error;
      }

      //Escaped values for database insert
      $firstnameEscaped = $this->mysqli->real_escape_string($firstname);
 			$middlenameEscaped = $this->mysqli->real_escape_string($middlename);
 			$lastnameEscaped = $this->mysqli->real_escape_string($lastname);
      $emailEscaped = $this->mysqli->real_escape_string($email);
      $usernameEscaped = $this->mysqli->real_escape_string($username);
      $passwordEscaped = $this->mysqli->real_escape_string($password);
      $passwordHashed = password_hash($passwordEscaped, PASSWORD_BCRYPT);

      //Inserts new account into the database, with hashed password
			$sql = "INSERT INTO Customer (firstname, middlename, lastname, email, username, passwordHash) VALUES ('$firstnameEscaped', '$middlenameEscaped', '$lastnameEscaped', '$emailEscaped', '$usernameEscaped', '$passwordHashed')";

			if (! $result = $this->mysqli->query($sql)) {
				$this->error = $this->mysqli->error;
			}

    	return $this->error;
    }


    //Not yet funcitonal
    public function login(){
        if(!$_POST('username')){
          $this->HandleError("Username is empty.");
          return false;
        }

        if(!$_POST('password')){
          $this->HandleError("Password is empty.");
          return false;
        }

        $username = $this->mysqli->real_escape_string($_POST['username']);
        $password = $this->mysqli->real_escape_string($_POST['password']);

        if(!$this->verifyInDB($username, $password)){
          return false;
        }

        $_SESSION[$this->GetLoginSessionVar()] = $username;
        return true;
    }

    //Not yet functional
    public function verifyInDb($username = '', $password = ''){
      $passwordVerify = password_verify($password, $passwordHashed);
      $sql = "Select name, email from customer ".
        " where username='$username' and password='$passwordVerify' ";
      if (! $result = $this->mysqli->query($sql)) {
				$this->error = $this->mysqli->error;
			}
      else {
        print "Login Successful";
      }
    }

  }
?>
