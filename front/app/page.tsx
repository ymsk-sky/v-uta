"use client"

import { Box } from "@mui/material";
import Header from "./components/Header";
import SongList from "./components/SongList";
import RegisterButton from "./components/RegisterButton";

export default function Home() {
    return (
        <Box sx={{ display: "flex", flexDirection: "column", height: "100vh" }}>
            <Header/>
            <SongList/>
            <RegisterButton/>
        </Box>
    )
}
