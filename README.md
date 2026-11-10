# RiskMind Session 1 — Presentation + Prompter

| File | What it is |
|---|---|
| `Session 1/RiskMind Session 1.html` | The presentation the audience sees |
| `Session 1/RiskMind Session 1 Prompter.html` | Your teleprompter. It drives the presentation and shows the script |
| `Session 1/RiskMind Session1 Outline.html` | The outline: what to say at each beat. Edit this one |
| `build_prompter.py` | Copies the script from the outline into the prompter |

## Update the prompter after the outline changes

The script in the prompter comes from `Session 1/RiskMind Session1 Outline.html`.
The prompter does **not** pick up changes on its own. After you edit the outline:

1. Open Terminal.
2. Run these two lines:

   ```bash
   cd ~/Downloads/"RiskMind Video"
   python3 -I build_prompter.py
   ```

3. You should see a line like:

   ```
   12 scenes, 45 beats (Cover, Course, 1 … 43) -> .../RiskMind Session 1 Prompter.html
   ```

4. Reload the prompter in the browser (Cmd+R).

If you move or rename the outline or the prompter, pass both paths (outline first, then prompter):

```bash
python3 -I build_prompter.py "path/to/Outline.html" "path/to/Prompter.html"
```

**Check after rebuilding:** open the prompter with the presentation connected. If a yellow
warning says the beat counts don't match, the outline and the presentation have a different
number of beats. Fix the outline (one row per beat) and run the script again.

How beats line up with the presentation: each beat in the outline is one press of →.
A first beat labelled with a word (like `Cover`) is the frame shown before anything plays.

## Present

1. Keep the presentation and the prompter together in `Session 1/`, and use Chrome.
2. Open `Session 1/RiskMind Session 1 Prompter.html` and click **Open Presentation Window**.
3. Move the presentation window to the projector / second screen (or share it in Teams) and press **F** for full screen.
4. Click back on the prompter so it has keyboard focus.

| Key (in the prompter) | Does |
|---|---|
| → ↓ Space PageDown | Play the next beat (while playing: jump to the end of this beat) |
| ← ↑ PageUp | Back one beat |
| P | Pause / resume |
| Home | Back to the start |
| R | Show / hide the notes (Reference) |
| + / − | Text size |
| Click a beat | Replay it from its start |

Keys pressed in the presentation window sync back to the prompter too.
Don't minimise or fully cover the presentation window: Chrome pauses its animation when it can't be seen.
