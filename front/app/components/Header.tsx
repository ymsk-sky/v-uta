import { AppBar, Box, Toolbar, Typography } from "@mui/material";

export default function Header() {
    return (
        <Box>
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="h6" component="div">
                        V-UTA
                        </Typography>
                </Toolbar>
            </AppBar>
        </Box>
    )
}
