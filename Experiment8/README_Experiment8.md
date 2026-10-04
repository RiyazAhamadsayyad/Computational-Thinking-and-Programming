# Experiment 8: Asynchronous Web Crawler

## Aim

To implement an **asynchronous web crawler** in Python using `asyncio` and `aiohttp`, and measure the time taken to fetch multiple URLs concurrently.

## Concepts Used

- Asynchronous Programming
- `asyncio`
- `aiohttp`
- Coroutines
- `async/await`
- Concurrent Execution
- Exception Handling
- Retry Mechanism

## Requirements

Install `aiohttp` before running the program:

```bash
pip install aiohttp
```

## Program

```python
import asyncio
import aiohttp
import time

urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net"
]

async def fetch(session, url):
    for _ in range(3):
        try:
            async with session.get(url, timeout=5) as r:
                return r.status
        except:
            await asyncio.sleep(1)
    return "Failed"

async def async_crawler():
    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(
            *(fetch(session, url) for url in urls)
        )

start = time.time()
result = asyncio.run(async_crawler())
print("Async:", result)
print("Time:", round(time.time() - start, 2), "seconds")
```

## Sample Output

The exact execution time may vary depending on the internet connection and server response.

```text
Async: [200, 200, 200]
Time: 0.65 seconds
```

`200` indicates that the HTTP request was successful.

## Explanation

### 1. URL List

Three URLs are stored in a list:

```python
urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net"
]
```

### 2. Asynchronous Fetch Function

```python
async def fetch(session, url):
```

This function sends an HTTP request asynchronously.

```python
async with session.get(url, timeout=5) as r:
    return r.status
```

The HTTP response status code is returned.

### 3. Retry Mechanism

Each URL is attempted up to three times:

```python
for _ in range(3):
```

If a request fails, the program waits for one second before retrying:

```python
await asyncio.sleep(1)
```

If all attempts fail, it returns:

```text
Failed
```

### 4. Concurrent Execution

The program uses:

```python
await asyncio.gather(
    *(fetch(session, url) for url in urls)
)
```

`asyncio.gather()` runs the multiple fetch operations concurrently.

```text
Without Async:

URL 1 ─────────→
                 URL 2 ─────────→
                                  URL 3 ─────────→

With Async:

URL 1 ─────────→
URL 2 ─────────→
URL 3 ─────────→
```

### 5. Event Loop

```python
result = asyncio.run(async_crawler())
```

`asyncio.run()` starts the asynchronous event loop and executes the crawler.

## Important Functions

| Function | Purpose |
|---|---|
| `async def` | Defines an asynchronous function |
| `await` | Waits for an async operation without blocking |
| `asyncio.gather()` | Runs multiple coroutines concurrently |
| `asyncio.run()` | Runs the asynchronous program |
| `aiohttp.ClientSession()` | Creates an HTTP session |
| `asyncio.sleep()` | Performs a non-blocking delay |

## Advantages

- Fetches multiple URLs concurrently.
- Suitable for I/O-bound operations.
- Does not block while waiting for network responses.
- Efficient for handling many network requests.
- Retry mechanism improves reliability.

## Result

The asynchronous web crawler was successfully implemented using **`asyncio` and `aiohttp`**. Multiple URLs were fetched concurrently and the total execution time was measured.
