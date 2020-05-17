
resource "sym_flow" "infra_access" {
  meta = {
    strategies = sym_strategies.escalation_strategies
  }

  handler = {
    parent = "sym:approval"
    hooks = file("infra_access.py")
  }
}

resource "sym_strategies" "escalation_strategies" {
  // Add your escalation strategies here
}
