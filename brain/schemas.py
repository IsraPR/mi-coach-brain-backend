from typing import List
from pydantic import BaseModel, Field


class Summary(BaseModel):
    """High-level summary of the user's current career state. Pure data — no narrative."""

    current_role: str = Field(
        description="User's current or most recent role title, exactly as provided"
    )
    target_role: str = Field(
        description="The specific target role the user wants to reach"
    )
    strong_count: int = Field(
        description="Count of items where user is already strong",
        ge=0,
        default=0,
    )
    growth_count: int = Field(
        description="Count of items that need moderate to significant improvement",
        ge=0,
        default=0,
    )
    blocker_count: int = Field(
        description="Count of critical blockers right now", ge=0, default=0
    )
    fastest_route_message: str = Field(
        description="One clear, direct sentence answering: 'What is the main thing currently holding this person back from the target role?'"
    )


class Insight(BaseModel):
    """Structured evaluation of ONE requirement / skill / experience from the provided data."""

    title: str = Field(
        description="Name of the skill, capability or experience — use the exact or very close wording from user data / available steps"
    )
    status: str = Field(
        description="Current user level vs this item. Use realistic terms based on evidence (strong / good / moderate / weak / blocker / critical gap / etc.)"
    )
    role_requirement_status: List[str] = Field(
        description="How important this is for the target role (e.g. 'required', 'critical', 'important', 'helpful', 'nice-to-have') — base on data",
        default_factory=list,
    )
    why_blocking: str = Field(
        description="Concise reason why this is (or isn't) currently a blocker. Use '' if it is not blocking."
    )
    feedback_evidence: List[str] = Field(
        description="Specific quotes, scores, facts or examples from 360 feedback, resume or conversation that justify the status",
        default_factory=list,
    )
    next_checkpoint: str = Field(
        description="Concrete, observable next milestone or proof point for improving this item"
    )


class MapNode(BaseModel):
    """One node in the career map — must be derived from something present in the user data."""

    id: str = Field(
        description="Unique, stable identifier for this node (kebab-case recommended, e.g. 'distributed-systems', 'stakeholder-management-2')"
    )
    label: str = Field(
        description="Short, user-friendly display name (4-8 words max)"
    )
    type: str = Field(
        description="Kind of node (skill / experience / certification / behavior / project / etc.) — match language from input data"
    )
    category: str = Field(
        description="Broader grouping if applicable (technical / leadership / communication / domain / etc.) — use terms from data when possible"
    )
    route_position: int = Field(
        description="Suggested position in the fastest path: 0 = already strong, 1 = most urgent next, 2 = medium-term, 3+ = longer term",
        ge=0,
    )
    connected_to: List[str] = Field(
        description="IDs of nodes that become reachable / easier after completing this one",
        default_factory=list,
    )
    description: str = Field(
        description="2-4 sentence practical explanation of what this node represents"
    )
    insight: Insight = Field(
        description="Gap analysis for this node — strictly evidence-based"
    )


class CareerMap(BaseModel):
    """
    Structured career gap analysis derived from the user's data, focused on the path from current_role to target_role.
    """

    summary: Summary
    map_nodes: List[MapNode] = Field(
        description="All relevant progression nodes derived from the data (usually 6-10). Include already-strong items (route_position=0)."
    )


class NextSteps(BaseModel):
    """
    Highly specific, actionable next steps for the user based on the CareerMap and available steps.
    """

    focus_area: str = Field(
        description="One-sentence name of the #1 area to focus on right now"
    )
    best_next_move: str = Field(
        description="Most impactful concrete action the user should take next — must come from available_steps"
    )
    why_now: str = Field(
        description="Why this move has the highest leverage at this moment — explicitly connect to blockers or gaps from the CareerMap"
    )
    expected_evidence: List[str] = Field(
        description="Specific, observable proofs that the action has been completed successfully",
        default_factory=list,
    )
    success_looks_like: List[str] = Field(
        description="2-5 clear descriptions of what good performance or outcome looks like",
        default_factory=list,
    )
    unlocks: List[str] = Field(
        description="Node IDs from the CareerMap that this action helps complete or advance",
        default_factory=list,
    )
    can_wait: List[str] = Field(
        description="Important items / nodes / steps that can safely be postponed 3-9 months",
        default_factory=list,
    )


class CareerPathResponse(BaseModel):
    """Final combined output structure — used only in your application code to merge both agents."""

    message: str = Field(default="Career path generated successfully.")
    career_map: CareerMap
    next_steps: NextSteps
