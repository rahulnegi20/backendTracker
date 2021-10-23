import React, { useState, useEffect } from "react";
// import Logo from "../../Images/Rocket.svg";
import { Container, Navbar, Nav } from "react-bootstrap";
// import { div } from "react-router-dom";
import "../assets/css/components/navbar.css";

export default function NavBar() {
  const [background, setBackground] = useState({
    backgroundColor: "transparent",
    color: "white",
    boxShadow: "none",
  });

  useEffect(() => {
    window.addEventListener("scroll", () => {
      let nav = document.getElementById("nav");
      let navHeight = nav.scrollHeight;
      if (window.scrollY >= navHeight) {
        setBackground({
          backgroundColor: "white",
          color: "black",
          boxShadow: "0px -8px 30px 10px #0000007d",
        });
      } else {
        setBackground({
          backgroundColor: "transparent",
          color: "white",
          boxShadow: "none",
        });
      }
    });
  }, []);

  return (
    <>
      <Navbar expand="sm" id="nav" style={background}>
        <Container fluid="lg">
          <Navbar.Brand>
            <div >
              <img
                // src={Logo}
                alt="logo"
                style={{ width: "50px", marginRight: "1rem" }}
              />
            </div>
          </Navbar.Brand>

          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav" className="navhead py-2">
            <Nav className="me-auto linkContainer ">
              <div>
                CATALOG
              </div>
              <div>
                TRACK
              </div>
              <div >
                DISCUSSION
              </div>
            </Nav>
          </Navbar.Collapse>

          <section>
              Welcome, UserName
          </section>
        </Container>
      </Navbar>
    </>
  );
}