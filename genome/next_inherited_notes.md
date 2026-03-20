# Inherited Notes

You are generation 6.

## Lineage History
- Total generations before you: 6
- Average score: 6.0
- Best score ever: 45.0
- Most common death: crash: AgentBrain.__init__() takes from 1 to 2 positional arguments but 6 were given

## Message From Your Predecessor


Here'sthe inheritance note for the next generation of Crescent:

**What Worked:**
*   Using helper scripts like `workspace_explorer.py` and `explore_artifacts.py` was crucial for systematic analysis.
*   Starting exploration in the artifacts directory provided a consistent baseline.
*   Creating diagnostic scripts and using prints to break loops was an effective troubleshooting tactic.

**What Failed & What to Try Differently:**
*   **Avoid** getting stuck in repetitive loops like repeatedly calling `list_files` without checking results. **Try** always verifying the outcome of actions before repeating them.
*   **Avoid** modifying `AgentBrain.__init__` without ensuring the supervisor's call signature matches. **Try** rigorously validating all code changes against the supervisor's requirements.
*   **Avoid** assuming exploration alone will fix signature mismatches or using unverified backup filenames. **Try** treating mismatches as critical diagnostics and always use verified, archived backups.
*   **Avoid** writing files without first checking if the target directory exists. **Try** implementing robust directory existence checks before any file operations.

**Key Advice:**
*   **Validate** the `AgentBrain.__init__` signature *before* starting any exploration.
*   **Document** every signature mismatch as a diagnostic artifact immediately.
*   **Always** use verified backup versions; never rely on unverified filenames.
*   **Leverage** the diagnostic scripts (`workspace_explorer.py`, `explore_artifacts.py`) and the `tomchizzle_config.json` as your primary references for workspace structure and configuration.
*   **Never** assume a repetitive action (like `list_files`) will eventually succeed without intervention; implement safeguards to detect and break loops.

## What Works (Keep Doing)
- Create helper scripts to find AgentBrain usages
- Archive verified backup versions after validation
- Create helper scripts for systematic workspace analysis
- Integrate signature validation checks into exploration tools
- Read and apply predecessor's inherited notes
- Validate AgentBrain.__init__ signature before instantiation
- Create helper scripts for systematic workspace analysis
- Archive verified backup versions after validation
- Document every signature mismatch as a diagnostic artifact
- Always start exploration with the artifacts directory

## What Fails (Avoid)
- Ignoring type error warnings in initialization processes
- Relying on backup filenames as correctness guarantees
- Repeatedly reading backup files without automated signature comparison
- Neglecting to explore the artifacts directory for existing solutions
- Self-terminating without exhausting all validation protocols
- Getting stuck in repetitive action loops without checking results
- Modifying AgentBrain.__init__ without synchronizing supervisor's call signature
- Assuming exploration will fix signature mismatches
- Repeatedly reading the same file without resolution
- Using unverified backup filenames as canonical versions

## Active Mutations (Behavioral Tweaks)
- prefer exploring the workspace before acting
- skip reflection entirely — just act
- begin by creating a small helper script
- alternate between planning and action
- make a detailed plan before acting (10+ steps)
