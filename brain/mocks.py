MOCK_CAREER_PATH_RESPONSE = {
    "message": "Career path generated successfully (MOCKED when test_mode: true).",
    "career_map": {
        "summary": {
            "current_role": "Mid Backend Engineer",
            "target_role": "Senior Backend Engineer",
            "strong_count": 3,
            "growth_count": 2,
            "blocker_count": 1,
            "fastest_route_message": "Turn strong execution into visible senior-level influence by improving stakeholder communication and creating proof of mentorship.",
        },
        "map_nodes": [
            {
                "id": "quality-delivery",
                "label": "Quality Delivery",
                "type": "strong",
                "category": "signal",
                "route_position": 1,
                "connected_to": [
                    "ownership",
                    "technical-execution",
                    "manager-review",
                ],
                "description": "Alex consistently ships reliable backend work with low churn and strong operational follow-through.",
                "insight": {
                    "title": "Quality Delivery is already a trusted strength",
                    "status": "Strong signal",
                    "role_requirement_status": [
                        "Delivery reliability already supports the next-level expectation.",
                        "Execution quality is not the limiting factor in the promotion path.",
                        "This signal should now be converted into broader influence.",
                    ],
                    "why_blocking": "This is not blocking the route. The risk is that strong execution stays invisible as leverage if it is not paired with communication and architectural framing.",
                    "feedback_evidence": [
                        "Managers see Alex as dependable on important backend work.",
                        "Production changes tend to land with solid quality and follow-through.",
                        "Quality is visible in results, but less visible in promotion narrative artifacts.",
                    ],
                    "next_checkpoint": "Use the credibility from delivery quality to lead one decision note or walkthrough, not just another implementation.",
                },
            },
            {
                "id": "ownership",
                "label": "Ownership",
                "type": "strong",
                "category": "signal",
                "route_position": 2,
                "connected_to": [
                    "quality-delivery",
                    "system-design",
                    "stakeholder-communication",
                    "one-on-one-notes",
                ],
                "description": "Peers trust Alex to take ambiguous work and drive it toward delivery without needing constant oversight.",
                "insight": {
                    "title": "Ownership is strong, but it needs wider visibility",
                    "status": "Strong signal",
                    "role_requirement_status": [
                        "Ownership already signals trusted scope handling.",
                        "Senior readiness improves when ownership includes more decision communication.",
                        "This strength can become a bridge into stakeholder confidence.",
                    ],
                    "why_blocking": "Ownership alone is not blocking the route. The route slows down when ownership is visible only inside engineering execution rather than across stakeholders and decision points.",
                    "feedback_evidence": [
                        "Alex takes responsibility for ambiguous work and keeps momentum moving.",
                        "Scope handling is strong, but business-facing framing is less visible.",
                        "Peers experience ownership directly; leadership may only see outcomes.",
                    ],
                    "next_checkpoint": "Turn one owned backend initiative into a story with tradeoffs, risks, and decision framing that others can reuse.",
                },
            },
        ],
    },
    "next_steps": {
        "focus_area": "Stakeholder Communication",
        "best_next_move": "Write and present a one-page backend design note for the next meaningful technical change.",
        "why_now": "Alex already has strong delivery credibility. The fastest path to Senior Backend Engineer is to make technical judgment and tradeoff communication more visible to engineering peers, product partners, and leadership.",
        "expected_evidence": [
            "A shareable artifact that explains context, options, recommendation, and rollout risk.",
            "A clearer connection between backend work and product or business impact.",
            "Feedback from stakeholders that Alex's technical thinking is easier to follow and trust.",
        ],
        "roadmap": {
            "now": [
                "Choose one upcoming backend change with real tradeoffs.",
                "Draft a concise design note with options, recommendation, and risk framing.",
                "Ask a manager or senior peer to review the clarity of the narrative, not just the technical correctness.",
            ],
            "next": [
                "Present the note in a cross-functional walkthrough with product or engineering partners.",
                "Capture follow-up questions and convert them into reusable FAQ or rollout notes.",
                "Use PR descriptions and project updates to reinforce the same stakeholder-friendly language.",
            ],
            "then": [
                "Repeat the pattern on a second project to show consistency.",
                "Pair the stronger communication signal with clearer mentorship moments in reviews and design discussions.",
                "Turn repeated artifacts into evidence for promotion conversations.",
            ],
        },
        "success_looks_like": [
            "Alex is invited into conversations earlier because stakeholders trust the framing, not just the execution.",
            "At least one design artifact becomes part of the promotion evidence set.",
            "Managers can point to visible examples of influence beyond direct coding output.",
        ],
        "unlocks": [
            "Stronger system design credibility",
            "Better promotion narrative",
            "Higher-trust cross-functional collaboration",
        ],
        "can_wait": [
            "Deep specialization in a brand-new backend domain",
            "A large personal rebrand effort",
            "Broad process optimization outside Alex's current scope",
        ],
    },
}
