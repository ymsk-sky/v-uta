import { useEffect, useState } from "react";
import { Box, Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from "@mui/material";
import YouTubeIcon from "@mui/icons-material/YouTube";
import TuneIcon from "@mui/icons-material/Tune";

interface VideoRecord {
    song_title: string,
    original_artist: string,
    vtuber_name: string,
    vtuber_agency: string,
    video_type: string,
    urls: string[],
}

interface FilteredRecord {
    song_title: string | null,
    original_artist: string | null,
    vtuber_name: string | null,
    vtuber_agency: string | null,
    video_type: string | null,
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

    const fetchFilteredRecords = async (param: FilteredRecord) => {
        try {
            const response = await fetch("http://localhost:8000/records", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(param),
            });
            if (!response.ok) {
                throw Error("Fetch Error");
            }
            const records: VideoRecord[] = await response.json();
            setVideoRecords(records);
        } catch (error) {
            console.log("error");
            setVideoRecords([]);
        }
    };

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
                                <TableCell key={column}>
                                    {column === "urls" ? (
                                        <Box sx={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                                            {column}
                                            <Button variant="text" sx={{ color: "#222222" }} onClick={() => { console.log("clicked") }}>
                                                <TuneIcon/>
                                            </Button>
                                        </Box>
                                    ) : (
                                        column
                                    )}
                                </TableCell>
                            ))}
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {videoRecords.map((record, index) => (
                            <TableRow key={index}>
                                <TableCell component="th" scope="row">
                                    {index}
                                </TableCell>
                                <TableCell>
                                    <Button variant="text" onClick={() => {
                                        const param: FilteredRecord = {
                                            song_title: record.song_title,
                                            original_artist: null,
                                            vtuber_name: null,
                                            vtuber_agency: null,
                                            video_type: null,
                                        }
                                        fetchFilteredRecords(param)}
                                    } sx={{ color: "black" }}>
                                        {record.song_title}
                                    </Button>
                                </TableCell>
                                <TableCell>
                                    <Button variant="text" onClick={() => {
                                        const param: FilteredRecord = {
                                            song_title: null,
                                            original_artist: record.original_artist,
                                            vtuber_name: null,
                                            vtuber_agency: null,
                                            video_type: null,
                                        }
                                        fetchFilteredRecords(param)}
                                    } sx={{ color: "black" }}>
                                        {record.original_artist}
                                    </Button>
                                </TableCell>
                                <TableCell>
                                    <Button variant="text" onClick={() => {
                                        const param: FilteredRecord = {
                                            song_title: null,
                                            original_artist: null,
                                            vtuber_name: record.vtuber_name,
                                            vtuber_agency: null,
                                            video_type: null,
                                        }
                                        fetchFilteredRecords(param)}
                                    } sx={{ color: "black" }}>
                                        {record.vtuber_name}
                                    </Button>
                                </TableCell>
                                <TableCell>
                                    <Button variant="text" onClick={() => {
                                        const param: FilteredRecord = {
                                            song_title: null,
                                            original_artist: null,
                                            vtuber_name: null,
                                            vtuber_agency: record.vtuber_agency,
                                            video_type: null,
                                        }
                                        fetchFilteredRecords(param)}
                                    } sx={{ color: "black" }}>
                                        {record.vtuber_agency}
                                    </Button>
                                </TableCell>
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
