param(
    [Parameter(Mandatory = $true)]
    [string]$Instance,

    [Parameter(Mandatory = $true)]
    [string]$Zone,

    [string]$Project = "",
    [string]$RemoteDir = "/home/faris/crescent-agi"
)

$ErrorActionPreference = "Stop"

$projectArgs = @()
if ($Project) {
    $projectArgs = @("--project", $Project)
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$envExample = Join-Path $repoRoot ".env.example"

if (-not (Test-Path $envExample)) {
    throw ".env.example is missing from $repoRoot"
}

Write-Host "Preparing remote directory..."
& gcloud @projectArgs compute ssh $Instance --zone $Zone --command "mkdir -p $RemoteDir"

$copyItems = @(
    "core",
    "genome",
    "mutable",
    "seeds",
    "deploy",
    "main.py",
    "requirements.txt",
    "config.yaml",
    ".env.example",
    ".gitignore",
    ".gitattributes"
)

foreach ($item in $copyItems) {
    $localPath = Join-Path $repoRoot $item
    if (-not (Test-Path $localPath)) {
        throw "Missing expected deploy item: $localPath"
    }

    $scpArgs = @()
    if ((Get-Item $localPath) -is [System.IO.DirectoryInfo]) {
        $scpArgs += "--recurse"
    }

    Write-Host "Copying $item..."
    & gcloud @projectArgs compute scp @scpArgs `
        $localPath `
        "${Instance}:${RemoteDir}" `
        --zone $Zone
}

Write-Host "Provisioning VM runtime..."
& gcloud @projectArgs compute ssh $Instance --zone $Zone --command "chmod +x $RemoteDir/deploy/install_vm.sh && bash $RemoteDir/deploy/install_vm.sh $RemoteDir"
