import { Button, Form} from "react-bootstrap";
import "../../assets/css/Auth/login.css";

function Login() {
  return (
    <>
      <Form className="BasicLogin pt-4">
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control type="email" placeholder="Enter email" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control type="password" placeholder="Password" />
        </Form.Group>

        <Button id="loginbtn" type="submit">
          LOG IN
        </Button>
      </Form>
    </>
  );
}

export default Login;
