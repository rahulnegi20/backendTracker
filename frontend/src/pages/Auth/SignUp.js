import { Button, Form } from "react-bootstrap";
import "../../assets/css/Auth/signup.css";

export default function SignUp() {
  return (
    <div className="BasicSignUp pt-4">
      <Form>
        <Form.Group className="mb-3" controlId="formBasicName">
          <Form.Label>Full Name</Form.Label>
          <Form.Control type="email" placeholder="Enter your name" />
        </Form.Group>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control type="email" placeholder="Enter email" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Create Password</Form.Label>
          <Form.Control type="password" placeholder="Enter your password" />
        </Form.Group>
        <Button id="signbtn" type="submit">
          SIGN UP
        </Button>
      </Form>
    </div>
  );
}
