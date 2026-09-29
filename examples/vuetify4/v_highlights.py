import trame_server
from trame.app import TrameApp
from trame.decorators import change

from trame.ui.vuetify4 import SinglePageLayout
from trame.widgets import html
from trame.widgets import vuetify4 as v4

v4.enable_lab()


def fuzzy(text: str, query: str) -> bool:
    """Return True if every char of query appears in text in order."""
    it = iter(text.lower())
    return all(ch in it for ch in query.lower())


class HighlightsExample(TrameApp):
    def __init__(self, server: trame_server.Server | str | None = None) -> None:
        super().__init__(server)

        self.state.terms = []
        self.state.matching_profile = ""
        self.state.profiles = [
            (
                "Sarah specializes in Python and Go, building AST-driven linters and code analyzers. "
                "She has deep experience refactoring TypeScript monorepos into modular architectures. "
                "Her current focus is a Python-based static analysis pipeline that feeds into Go "
                "microservices."
            ),
            (
                "Marcus works on a Python-to-Rust compilation target, specializing in AST "
                "transformations and type inference. He previously built a JavaScript bundler "
                "from scratch, optimizing module graph traversal. His side project extends "
                "Rust's parser to support embedded Python scripting."
            ),
            (
                "Priya builds enterprise dashboards in TypeScript and Java, with heavy use of "
                "AST-based code generators for API clients. She maintains a Go service mesh "
                "that proxies traffic between Java and TypeScript tiers. Her team's linter "
                "pipeline spans TypeScript, Java, and Go codebases."
            ),
            (
                "Lena designs CLI tools in Python and TypeScript that emit human-readable AST "
                "diagnostics for developers. She previously worked on a Ruby-based code "
                "migration framework that relied on AST pattern matching. Her current role "
                "bridges Python scripting and TypeScript frontend tooling."
            ),
            (
                "Tom writes infrastructure-as-code in Go and Rust, with a focus on AST "
                "validation for declarative config formats. He maintains a JavaScript "
                "build pipeline that parses source ASTs to inject telemetry. His weekend "
                "project is a Rust-based Python interpreter that reuses CPython's AST node "
                "definitions."
            ),
        ]

        self._build_ui()

    def _build_ui(self) -> None:
        with SinglePageLayout(self.server) as layout:
            with layout.content:
                v4.VCombobox(
                    v_model="terms",
                    label="Highlight terms",
                    chips=True,
                    closable_chips=True,
                    hide_details=True,
                    multiple=True,
                    classes="mb-6 mt-4",
                    variant="outlined",
                )
                v4.VHighlight(
                    v_if="matching_profile.length > 0",
                    query=("terms",),
                    text=("matching_profile",),
                )
                with html.Div(v_if="matching_profile.length == 0"):
                    html.P(v_for="profile in profiles", children="{{ profile }}")

    @change("terms")
    def update_results(self, **_kwargs):
        queries = [q.strip() for q in self.state.terms if q and q.strip()]
        if not queries:
            self.state.matching_profile = ""
            return

        scored = [
            (item, sum(1 for q in queries if fuzzy(item, q)))
            for item in self.state.profiles
        ]

        best = sorted(
            (s for s in scored if s[1]),
            key=lambda s: s[1],
            reverse=True,
        )
        self.state.matching_profile = best[0][0] if best else ""


def main():
    app = HighlightsExample()
    app.server.start()


if __name__ == "__main__":
    main()
