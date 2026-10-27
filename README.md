# EV Market Performance & Insights

A complete starter project built using the supplied electric-vehicle market CSVs.

## Start here
- **Dashboard:** open `index.html` in Chrome. The charts and data are embedded in the HTML; it does not need an internet connection or a local JSON server.
- **Report:** read `PROJECT_REPORT.md` or `reports/PROJECT_REPORT.md`.
- **Analysis script:** `analysis/analyze_ev_market.py`.
- **Tableau instructions:** `TABLEAU_GUIDE.md`.
- **Data:** `data/ev_market_train.csv` and `data/ev_market_test.csv`.

## Dataset facts
- Training: 200,000 rows × 37 columns.
- Test: 100,000 rows × 37 columns.
- Average range: 324.5 km.
- Average listed price: $64,921.
- Average customer rating: 4.09/5.
- Missing cells in training dataset: 18,996.

## Run the Python analysis
Install Python 3 and run:
```bash
pip install pandas
python analysis/analyze_ev_market.py
```

## Upload to GitHub and publish a demo
1. Extract this ZIP.
2. Create a public GitHub repository.
3. Upload the contents of this folder (not the ZIP file itself). Keep `index.html` in the repository root.
4. In GitHub, open **Settings → Pages**.
5. Select **Deploy from a branch**, branch `main`, folder `/(root)`, and Save.
6. After publishing, GitHub Pages shows a URL like `https://YOUR-USERNAME.github.io/REPOSITORY-NAME/`.
7. Paste that URL into SkillWallet's **Demo Link** field. Paste `https://github.com/YOUR-USERNAME/REPOSITORY-NAME` into **GitHub Link**.

## Submission note
The HTML dashboard is a browser preview, not a native Tableau workbook. To submit an actual Tableau dashboard, follow `TABLEAU_GUIDE.md` and publish your workbook to Tableau Public. Do not claim the Tableau workbook has been published until you have done so.
