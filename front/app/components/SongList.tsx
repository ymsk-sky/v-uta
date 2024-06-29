import { useEffect, useState } from "react";
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from "@mui/material";

function createData(
    id: number,
    song: string,
    original_artist: string,
    vtuber: string,
    agency: string,
    urls: string[],
) {
    return { id, song, original_artist, vtuber, agency, urls };
}

const columns = ["id", "song", "artist", "vtuber", "agency", "urls"];

const rows = [
    createData(0, "MySong", "Artist00", "Hanako", "V-Test", ["qwertyu"]),
    createData(1, "YourSong", "Artist01", "Taro", "V-Test", ["asdfghj"]),
    createData(2, "ThemSong", "Artist02", "Momo", "V-Temp", ["zxcvbnm"]),
];

const fetchData = async (setData: Function) => {
    await fetch("http://localhost:8000")
        .then((res) => res.json())
        .then(json => {
            // WIP: rowsに入れる
            json.map((data: object) => {
                console.log(data);
            });
        });
};

export default function SongList() {
    const [rowsx, setRows] = useState();

    useEffect(() => {
        fetchData(setRows);
    }, []);

    return (
        <TableContainer>
            <Table>
                <TableHead>
                    <TableRow>
                        {columns.map((column) => (
                            <TableCell>{column}</TableCell>
                        ))}
                    </TableRow>
                </TableHead>
                <TableBody>
                    {rows.map((row) => (
                        <TableRow key={row.id}>
                            <TableCell component="th" scope="row">
                                {row.id}
                            </TableCell>
                            <TableCell>{row.song}</TableCell>
                            <TableCell>{row.original_artist}</TableCell>
                            <TableCell>{row.vtuber}</TableCell>
                            <TableCell>{row.agency}</TableCell>
                            <TableCell>{row.urls}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    )
}
