package main

import "testing"

func Test_sum_oneplusone(t *testing.T) {
	expected := 2
	got := sum(1, 1)

	if got != expected {
		t.Errorf("expected: %d, got: %d", expected, got)

	}
}

func Test_sum_oneplustwo(t *testing.T) {
	expected := 3
	got := sum(1, 2)

	if got != expected {
		t.Errorf("expected: %d, got: %d", expected, got)

	}
}

// A more robust way of doing tests:

func Test_RangeOfValues(t *testing.T) {
	tables := []struct {
		testCase string
		x        int
		y        int
		expected int
	}{
		{"one and one", 1, 1, 2},
		{"even + odd", 1, 2, 3},
		{"even + even", 2, 2, 4},
	}
	for _, tc := range tables {
		t.Run(tc.testCase, func(t *testing.T) {
			got := sum(tc.x, tc.y)
			if got != tc.expected {
				t.Errorf("For (%d+%d) expected: %d, got: %d", tc.x, tc.y, tc.expected, got)

			}
		})
	}
}
