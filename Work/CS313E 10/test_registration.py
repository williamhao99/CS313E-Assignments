"""Registration Test Suite"""
import unittest
from registration import Graph


class TestGetRegistrationPlan(unittest.TestCase):
    """get_registration_plan Test Suite"""

    def check_registration_plan(self, graph, student_output):
        """
        Validate if the given grouped traversal is a valid topological sort.
        """
        n = len(graph.adjacency_matrix)

        position = {}
        flattened_registration_plan = []
        for group in student_output:
            flattened_registration_plan.extend(group)
        for i, course in enumerate(flattened_registration_plan):
            position[course] = i

        # Stores information about which semester
        semesters = {}
        for i, semester in enumerate(student_output):
            if len(semester) > 4:
                self.fail(f"Length of semester {i} exceeded 4: {semester}")
            if len(semester) == 0:
                self.fail(f"Length of semester {i} should not be 0.")
            for course in semester:
                semesters[course] = i

        labels = [graph.vertices[i].label for i in range(n)]

        actual, expected = set(flattened_registration_plan), set(labels)
        if len(actual) != len(expected):
            self.fail(
                "Length of registration plan does not match expected result. "
                f"actual: {len(actual)}, expected: {len(expected)}"
            )

        if actual != expected:
            self.fail(
                "Registration plan courses do not match expected result. "
                f"actual: {sorted(actual)}, expected: {sorted(expected)}"
            )

        for u in range(n):
            for v in range(n):
                if graph.adjacency_matrix[u][v] == 1:  # Edge u -> v exists
                    if semesters[labels[u]] == semesters[labels[v]]:
                        self.fail(
                            f"Prerequisite course {labels[u]} cannot be "
                            f"taken in the same semester as {labels[v]}"
                        )
                    if (
                        position[labels[u]] > position[labels[v]]
                    ):  # u must appear before v
                        self.fail(
                            f"Prerequisite course {labels[u]} was not "
                            f"taken before course {labels[v]}"
                        )

    def test_1(self):
        """Test get_registration_plan with 3 vertex, expecting a return of ["A"], ["B"], ["C"]."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(1, 2)  # B -> C
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_2(self):
        """Test get_registration_plan with 3 vertex, expecting a return of ["C", "B", "A"]."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_3(self):
        """Test get_registration_plan with 4 vertex, expecting a return of ["A"], ["C", "B"], ["D"]."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 3)  # B -> D
        graph.add_edge(2, 3)  # C -> D
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_4(self):
        """Test get_registration_plan with 4 vertex, expecting a return of ["A"], ["C", "B"], ["D"]."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(0, 3)  # A -> D
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_5(self):
        """Test get_registration_plan with 4 vertex, expecting a return of ["C", "A"], ["D", "B"]."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(2, 3)  # C -> D
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_6(self):
        """Test get_registration_plan with 10 vertex, expecting a return of ["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"]."""
        graph = Graph()
        for i in range(10):
            graph.add_vertex(str(i))
        for i in range(9):
            graph.add_edge(i, i + 1)  # 0 -> 1 -> 2 -> ... -> 9
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_7(self):
        """Test get_registration_plan with 4 vertex, expecting a return of ['D', 'A'], ['B'], ['C']."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(1, 2)  # B -> C
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_8(self):
        """Test get_registration_plan with 0 vertex, expecting a return of []."""
        graph = Graph()
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_9(self):
        """Test get_registration_plan with 3 vertex, expecting a return of ["A"], ["B"], ["C"]."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 2)  # B -> C
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_10(self):
        """Test get_registration_plan with 3 vertex, expecting a return of ["C"], ["B"], ["A"]."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_edge(2, 1)  # C -> B
        graph.add_edge(1, 0)  # B -> A
        result = graph.get_registration_plan()
        self.assertEqual(result, [["C"], ["B"], ["A"]])

    def test_11(self):
        """Test get_registration_plan with 5 vertex, diamond shape. Expecting [["A"], ["B", "C"], ["D"], ["E"]]."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_vertex("E")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 3)  # B -> D
        graph.add_edge(2, 3)  # C -> D
        graph.add_edge(3, 4)  # D -> E
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_12(self):
        """Test get_registration_plan with 6 vertex, all independent. Expecting 2D list with max 4 per semester."""
        graph = Graph()
        for label in ["A", "B", "C", "D", "E", "F"]:
            graph.add_vertex(label)
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_13(self):
        """Test get_registration_plan with 7 vertex, multiple chains merging. Expecting [["A", "B"], ["C", "D"], ["E"], ["F"], ["G"]]."""
        graph = Graph()
        for label in ["A", "B", "C", "D", "E", "F", "G"]:
            graph.add_vertex(label)
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 3)  # B -> D
        graph.add_edge(2, 4)  # C -> E
        graph.add_edge(3, 4)  # D -> E
        graph.add_edge(4, 5)  # E -> F
        graph.add_edge(5, 6)  # F -> G
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_14(self):
        """Test get_registration_plan with 8 vertex, binary tree shape. Expecting [["A"], ["B", "C"], ["D", "E", "F", "G"]]."""
        graph = Graph()
        for label in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            graph.add_vertex(label)
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 3)  # B -> D
        graph.add_edge(1, 4)  # B -> E
        graph.add_edge(2, 5)  # C -> F
        graph.add_edge(2, 6)  # C -> G
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_15(self):
        """Test get_registration_plan with 9 vertex, long chain + 1 branching. Expecting each course in new semester."""
        graph = Graph()
        for label in ["A", "B", "C", "D", "E", "F", "G", "H", "I"]:
            graph.add_vertex(label)
        for i in range(8):
            graph.add_edge(i, i + 1)  # Linear chain
        graph.add_edge(4, 6)  # Make it a DAG still by not completing a cycle (should be skipped if it's cyclic)
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)

    def test_16(self):
        """Test get_registration_plan with 12 vertex, 3 parallel chains of 4. Expecting [["A", "E", "I"], ["B", "F", "J"], ["C", "G", "K"], ["D", "H", "L"]]."""
        graph = Graph()
        for label in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]:
            graph.add_vertex(label)
        for i in range(0, 12, 4):
            graph.add_edge(i, i + 1)
            graph.add_edge(i + 1, i + 2)
            graph.add_edge(i + 2, i + 3)
        result = graph.get_registration_plan()
        self.check_registration_plan(graph, result)


class TestComputeDepth(unittest.TestCase):
    """compute_depth Test Suite"""

    def test_1(self):
        """Test compute_depth with 3 vertex and 2 edges."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(1, 2)  # B -> C
        graph.compute_depth()
        expected_depths = [2, 1, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_2(self):
        """Test get_registration_plan with 3 vertex and 0 edges"""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.compute_depth()
        expected_depths = [0, 0, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_3(self):
        """Test get_registration_plan with 4 vertex and 4 edges"""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 3)  # B -> D
        graph.add_edge(2, 3)  # C -> D
        graph.compute_depth()
        expected_depths = [2, 1, 1, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_4(self):
        """Test get_registration_plan with 4 vertex and 3 edges"""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(0, 3)  # A -> D
        graph.compute_depth()
        expected_depths = [1, 0, 0, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_5(self):
        """Test get_registration_plan with 4 vertex and 2 edges"""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(2, 3)  # C -> D
        graph.compute_depth()
        expected_depths = [1, 0, 1, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_6(self):
        """Test get_registration_plan with 10 vertex and 9 edges"""
        graph = Graph()
        for i in range(10):
            graph.add_vertex(str(i))
        for i in range(9):
            graph.add_edge(i, i + 1)  # 0 -> 1 -> 2 -> ... -> 9
        graph.compute_depth()
        expected_depths = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_7(self):
        """Test compute_depth with 4 vertex in a diamond shape DAG with an additional edge."""
        graph = Graph()
        graph.add_vertex("A") 
        graph.add_vertex("B") 
        graph.add_vertex("C") 
        graph.add_vertex("D")  

        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 3)  # B -> D
        graph.add_edge(2, 3)  # C -> D
        graph.add_edge(1, 2)  # B -> C 

        graph.compute_depth()
        expected_depths = [3, 2, 1, 0]  # A is deepest, D is a leaf
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_8(self):
        """Test get_registration_plan with 0 vertex"""
        graph = Graph()
        graph.compute_depth()
        expected_depths = []
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_9(self):
        """Test get_registration_plan with 3 vertex and 3 edges"""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 2)  # B -> C
        graph.compute_depth()
        expected_depths = [2, 1, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_10(self):
        """Test get_registration_plan with 3 vertex, expecting a return of ["C"], ["B"], ["A"]."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_edge(2, 1)  # C -> B
        graph.add_edge(1, 0)  # B -> A
        graph.compute_depth()
        expected_depths = [0, 1, 2]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_11(self):
        """Test compute_depth with 5 vertex, diamond shape."""
        graph = Graph()
        for label in ["A", "B", "C", "D", "E"]:
            graph.add_vertex(label)
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 3)  # B -> D
        graph.add_edge(2, 3)  # C -> D
        graph.add_edge(3, 4)  # D -> E
        graph.compute_depth()
        expected_depths = [3, 2, 2, 1, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_12(self):
        """Test compute_depth with 6 vertex, all independent."""
        graph = Graph()
        for label in ["A", "B", "C", "D", "E", "F"]:
            graph.add_vertex(label)
        graph.compute_depth()
        expected_depths = [0, 0, 0, 0, 0, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_13(self):
        """Test compute_depth with 7 vertex, multiple chains merging."""
        graph = Graph()
        for label in ["A", "B", "C", "D", "E", "F", "G"]:
            graph.add_vertex(label)
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 3)  # B -> D
        graph.add_edge(2, 4)  # C -> E
        graph.add_edge(3, 4)  # D -> E
        graph.add_edge(4, 5)  # E -> F
        graph.add_edge(5, 6)  # F -> G
        graph.compute_depth()
        expected_depths = [4, 4, 3, 3, 2, 1, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_14(self):
        """Test compute_depth with 8 vertex, binary tree shape."""
        graph = Graph()
        for label in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            graph.add_vertex(label)
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 3)  # B -> D
        graph.add_edge(1, 4)  # B -> E
        graph.add_edge(2, 5)  # C -> F
        graph.add_edge(2, 6)  # C -> G
        graph.add_edge(4, 7)  # E -> H (add an extra edge to increase depth)
        graph.compute_depth()
        expected_depths = [3, 2, 1, 0, 1, 0, 0, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_15(self):
        """Test compute_depth with 9 vertex, long chain + 1 branching."""
        graph = Graph()
        for label in ["A", "B", "C", "D", "E", "F", "G", "H", "I"]:
            graph.add_vertex(label)
        for i in range(8):
            graph.add_edge(i, i + 1)  # Linear chain
        graph.add_edge(4, 6)  # Branch from E -> G
        graph.compute_depth()
        expected_depths = [8, 7, 6, 5, 4, 3, 2, 1, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

    def test_16(self):
        """Test compute_depth with 12 vertex, 3 parallel chains of 4."""
        graph = Graph()
        for label in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]:
            graph.add_vertex(label)
        for i in range(0, 12, 4):
            graph.add_edge(i, i + 1)
            graph.add_edge(i + 1, i + 2)
            graph.add_edge(i + 2, i + 3)
        graph.compute_depth()
        expected_depths = [3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0]
        actual_depths = [v.depth for v in graph.vertices]
        self.assertEqual(expected_depths, actual_depths)

class TestHasCycle(unittest.TestCase):
    """has_cycle Test Suite"""

    def test_1(self):
        """Test has_cycle with 3 vertex and 2 edges, expecting a return of False."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(1, 2)  # B -> C
        self.assertFalse(graph.has_cycle())

    def test_2(self):
        """Test has_cycle with 2 vertex and 2 edges, expecting a return of True."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(1, 0)  # B -> A
        self.assertTrue(graph.has_cycle())

    def test_3(self):
        """Test has_cycle with 5 vertex and 5 edges, expecting a return of True."""
        graph = Graph()
        for i in range(5):
            graph.add_vertex(str(i))
        graph.add_edge(0, 1)  # 0 -> 1
        graph.add_edge(1, 2)  # 1 -> 2
        graph.add_edge(2, 3)  # 2 -> 3
        graph.add_edge(3, 4)  # 3 -> 4
        graph.add_edge(4, 0)  # 4 -> 0 (Cycle)
        self.assertTrue(graph.has_cycle())

    def test_4(self):
        """Test has_cycle with 4 vertex and 3 edges, expecting a return of False."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(2, 3)  # C -> D (No Cycle)
        self.assertFalse(graph.has_cycle())

    def test_5(self):
        """Test has_cycle with no edges, expecting a return of False."""
        graph = Graph()
        graph.add_vertex("A")
        self.assertFalse(graph.has_cycle())

    def test_6(self):
        """Test has_cycle with 3 vertex and 0 edges, expecting a return of False."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        self.assertFalse(graph.has_cycle())

    def test_7(self):
        """Test has_cycle with 4 vertex and 4 edges, expecting a return of False."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_vertex("E")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 3)  # B -> D
        graph.add_edge(2, 3)  # C -> D
        self.assertFalse(graph.has_cycle())

    def test_8(self):
        """Test has_cycle with 4 vertex and 4 edges, expecting a return of True."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_edge(0, 1)  # A -> B
        graph.add_edge(0, 2)  # A -> C
        graph.add_edge(1, 2)  # B -> C
        graph.add_edge(2, 3)  # C -> D
        self.assertFalse(graph.has_cycle())

if __name__ == "__main__":
    unittest.main()
