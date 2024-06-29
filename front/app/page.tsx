"use client"

import styles from "./page.module.css";
import SongList from "./components/SongList";

export default function Home() {
    return (
        <main className={styles.main}>
            <SongList/>
        </main>
    )
}
