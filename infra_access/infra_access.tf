provider "sym" {
  org = "healthy-health"
}

resource "sym_flow" "infra_access" {
  handler = {
    parent = "sym:approval"
    hooks = file("infra_access.py")
  }

  meta = {
    strategies = sym_strategies.escalation_strategies
  }
}

resource "sym_strategies" "escalation_strategies" {
  // Add your escalation strategies here
}
