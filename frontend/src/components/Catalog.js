import React from "react";
import { Container, Row, Col } from "react-bootstrap";

function Catalog() {
  return (
    <>
      <Container className="pt-3">
        <Row>
          <Col className="text-center">
            <h1>Catalog</h1>
          </Col>
        </Row>
        <Row>
            <Col><h3>Technology</h3></Col>
        </Row>
      </Container>
    </>
  );
}

export default Catalog;
