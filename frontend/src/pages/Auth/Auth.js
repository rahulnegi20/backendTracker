import React, { useState } from "react";
import "../../assets/css/Auth/auth.css";
import { ToggleButton, ToggleButtonGroup, Row, Col } from "react-bootstrap";
import Login from "./Login";
import SignUp from "./SignUp";

export default function Auth() {
  const [show, setshow] = useState(true);

  return (
    <>
      <div className="all p-5">
        <div className="flex-container p-1">
          <Row className="m-0">
            <Row className="left px-4">
              <Col className="p-4">
                <h1 id="header"className="text-center p-3">
                  Logo/Name
                </h1>

                <Row className="togglebtn">
                  <ToggleButtonGroup
                    id="btngrp"
                    type="radio"
                    name="options"
                    defaultValue={1}
                    size="lg"
                  >
                    <ToggleButton
                      style={{
                        background: "#949390",
                        border: "none",
                        padding: "5px 25px",
                      }}
                      id="tbg-radio-1"
                      value={1}
                      onClick={() => setshow(true)}
                    >
                      Log In
                    </ToggleButton>
                    <ToggleButton
                      style={{
                        background: "#aaa9a4",
                        border: "none",
                        padding: "5px 25px",
                      }}
                      id="tbg-radio-2"
                      value={2}
                      onClick={() => setshow(false)}
                    >
                      Sign Up
                    </ToggleButton>
                  </ToggleButtonGroup>
                </Row>
                <Row>
                  <Col className="">{show ? <Login /> : <SignUp />}</Col>
                </Row>
                <Row>
                  <Col>
                    <h3 id="or" className="pb-3">OR</h3>
                    <div className="google p-2">
                      
                      <span><img
                        src="https://www.freepnglogos.com/uploads/google-logo-png/google-logo-icon-png-transparent-background-osteopathy-16.png"
                        alt="google"
                      />CONTINUE WITH GOOGLE</span>
                    </div>
                  </Col>
                </Row>
              </Col>
            </Row>
            <Col className="right p-0"></Col>
          </Row>
        </div>
      </div>
    </>
  );
}
