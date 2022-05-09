import React from "react";
import Card from "./components/Card";


function Dashboard() {

    return (
        <div style={{
            display: 'flex',
            wrap: 'no-wrap',
        }}>
            <div style={{
                marginTop: '-15px',
                width: '20%',
                height: '100vh',
                backgroundColor: 'gray',
                borderColor: 'white',
                position: "-webkit-sticky",
                position: "sticky",
                top: "0",
            }}>
                ree
            </div>
            <div style={{
                width: '80%',
            }}>
                <div style={{
                    display: "flex",
                    flexWrap: "wrap",
                    justifyContent: "space-evenly"
                }}>
                    <Card props={{}}></Card>
                    <Card props={{}}></Card>
                    <Card props={{}}></Card>
                    <Card props={{}}></Card>
                    <Card props={{}}></Card>
                    <Card props={{}}></Card>
                    <Card props={{}}></Card>
                    <Card props={{}}></Card>
                </div>
            </div>
        </div>
    )
}
export default Dashboard;