import { useEffect, useState } from "react";
import { Box, Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from "@mui/material";
import YouTubeIcon from "@mui/icons-material/YouTube";

interface VideoRecord {
    song_title: string,
    original_artist: string,
    vtuber_name: string,
    vtuber_agency: string,
    video_type: string,
    urls: string[],
}

const columns = ["id", "song", "artist", "vtuber", "agency", "urls"];

const fetchRecords = async () => {
    const response = await fetch("http://localhost:8000");
    if (!response.ok) {
        throw new Error("Fetch Error");
    }
    const data: VideoRecord[] = await response.json();
    return data;
};

export default function SongList() {
    const [videoRecords, setVideoRecords] = useState<VideoRecord[]>([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const records = await fetchRecords();
                setVideoRecords(records);
            } catch (error) {
                console.log("error");
                setVideoRecords([]);
            }
        };
        fetchData();
    }, []);

    return (
        <Box sx={{
            flex: 1,
            overflow: "auto",
            marginTop: 4,
            marginX: 4,
            bgcolor: "background.default"
        }}>
            <TableContainer component={Paper}>
                <Table>
                    <TableHead sx={{ backgroundColor: "primary.light" }}>
                        <TableRow>
                            {columns.map((column) => (
                                <TableCell key={column}>{column}</TableCell>
                            ))}
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {videoRecords.map((record, index) => (
                            <TableRow key={index}>
                                <TableCell component="th" scope="row">
                                    {index}
                                </TableCell>
                                <TableCell>{record.song_title}</TableCell>
                                <TableCell>{record.original_artist}</TableCell>
                                <TableCell>{record.vtuber_name}</TableCell>
                                <TableCell>{record.vtuber_agency}</TableCell>
                                <TableCell>
                                    {record.urls.map((url) => (
                                        <Button variant="text" href={url} target="_blank" sx={{
                                            maxWidth: "30px",
                                            maxHeight: "30px",
                                            minWidth: "30px",
                                            minHeight: "30px",
                                            marginRight: 1
                                        }}>
                                            <YouTubeIcon sx={{ color: "#FF3D00" }}/>
                                        </Button>
                                    ))}
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    )
}
