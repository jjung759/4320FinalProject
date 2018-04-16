<?php
    require('LoginView.php');
    require('LoginModel.php');

    class LoginController {
      private $model;
      private $views;

      private $view = '';
      private $action = '';
  		private $message = '';

      public function __construct() {
  			$this->model = new LoginModel();
  			$this->views = new LoginViews();

  			$this->view = $_GET['view'] ? $_GET['view'] : 'loginView';
  			$this->action = $_POST['action'];
      }

      public function __destruct() {
  			$this->model = null;
  			$this->views = null;
      }

      public function run() {
  			if ($error = $this->model->getError()) {
  				print $views->errorView($error);
  				exit;
  			}

        switch($this->action) {
          case 'addAccount':
            $this->handleAddAccount();
            break;
          default:
            break;
        }

        switch($this->view) {
  				case 'addAccount':
  					print $this->views->addAccountForm($this->data, $this->message);
  					break;
          default: //LoginView
            if ($error) {
              $this->message = $error;
            }
            print $this->views->loginView($this->message);
            break;
        }
      }

      private function handleAddAccount() {
  			if($_POST['cancel']){
  				$this->view = 'loginView';
  				return;
  			}

  			$error = $this->model->addAccount($_POST);
  			if($error) {
  				$this->message = $error;
  				$this->view = 'addAccount';
  				$this->data = $_POST;
  			}
  		}
    }

?>
