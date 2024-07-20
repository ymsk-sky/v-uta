import { useEffect } from "react";
import { Box, Button } from "@mui/material";
import { VideoRecord, FilteredRecord } from "./SongList";

interface ModalProps {
    setShow: (show: boolean) => void;
    setVideoRecords: (records: VideoRecord[]) => void;
}

export default function FilterBox({setShow, setVideoRecords}: ModalProps) {
    useEffect(() => {
        console.log("filter box");
    }, []);

    const fetchFilteredRecords = async () => {
        const param: FilteredRecord = {
            song_title: null,
            original_artist: "HoneyWorks",
            vtuber_name: null,
            vtuber_agency: null,
            video_type: null,
        }
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
            console.log(error);
            setVideoRecords([]);
        }
        setShow(false);
    }

    return (
        <Box sx={{
            position: "fixed",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            backgroundColor: "rgba(0, 0, 0, 0.4)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
        }}>
            <Box sx={{
                zIndex: 2,
                width: "50%",
                padding: "1em",
                background: "#fff",
                p: 2,
            }}>
                <Box>
                    モーダル
                </Box>
                <Button variant="contained" onClick={() => fetchFilteredRecords()} sx={{ marginRight: 2 }}>
                    適用
                </Button>
                <Button variant="outlined" onClick={() => {
                    console.log("cancel");
                    setShow(false);
                }}>
                    キャンセル
                </Button>
            </Box>
        </Box>
    )
}
