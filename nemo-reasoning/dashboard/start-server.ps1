$PORT = 33304

# Find process using the port
$connection = Get-NetTCPConnection -LocalPort $PORT -ErrorAction SilentlyContinue

if ($connection) {
    $PID = $connection.OwningProcess
    Write-Host "Killing existing process on port $PORT (PID: $PID)"

    Stop-Process -Id $PID -Force
    Start-Sleep -Seconds 1
}

Write-Host "Starting server on http://localhost:$PORT/"

# Start server in background
$process = Start-Process uv `
    -ArgumentList "run", "python", "-m", "http.server", $PORT `
    -WindowStyle Hidden `
    -PassThru

Write-Host "Server running in background (PID: $($process.Id))"