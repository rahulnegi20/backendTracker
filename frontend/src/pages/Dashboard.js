import React from "react";
import "../assets/css/pages/Dashboard/dashboard.css";
import NavBar from "../components/Navbar";
// import { Container,Row,Col} from "react-bootstrap";
import Catalog from "../components/Catalog";

// import banner from "../assets/images/db4.png"

function Dashboard() {
  return (
    <>
      <NavBar />
      <section className="d-block w-100">
        <img
          className="banner"
        //   src={banner}
        // src="https://t4.ftcdn.net/jpg/02/54/80/61/360_F_254806104_LkAUKKFQLO4LNWofnCgSHxY9KCPCeZbp.jpg"
        src="https://lighthouse-tc.com/wp-content/uploads/2020/08/e-learning-header-bg.jpg"
        //   src="https://t3.ftcdn.net/jpg/04/00/77/64/360_F_400776431_5JxdDYRr1mn9yISiUFMPcLtLp3zt6NA1.jpg"
          alt="banner"
        />
      </section>
      <Catalog />
      {/* Catalog section */}
    </>
  );
}

export default Dashboard;
