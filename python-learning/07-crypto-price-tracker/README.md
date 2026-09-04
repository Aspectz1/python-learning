# Crypto Price Tracker

A CoinMarketCap project that repeatedly checks a cryptocurrency price and writes the results to `prices.csv`.

Press **Enter** to stop the tracker.

## Concepts practiced

- API requests
- JSON responses
- Nested lists/dictionaries
- `while` loops
- `for` loops
- `time.sleep()`
- Writing to a file
- Keyboard input

## Important

The API key is read from `CMC_API_KEY` so it is not stored in the repository.

`prices.csv` is ignored by Git because it is generated data.

## Windows PowerShell

```powershell
$env:CMC_API_KEY="YOUR_KEY"
python tracker.py
```
