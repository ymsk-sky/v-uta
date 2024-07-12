import { Button, Fab } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";

export default function RegisterButton() {
    return (
        <Fab
        color="primary"
        aria-label="add"
        onClick={() => {
            window.location.href = "http://localhost:3000/create";
        }}
        sx={{
            position: "fixed",
            bottom: 16,
            right: 16,
        }}>
            <AddIcon/>
        </Fab>
    )
}
