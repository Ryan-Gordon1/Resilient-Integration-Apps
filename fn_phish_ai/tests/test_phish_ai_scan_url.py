# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_phish_ai"
FUNCTION_NAME = "phish_ai_scan_url"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_phish_ai_scan_url_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("phish_ai_scan_url", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("phish_ai_scan_url_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestPhishAiScanUrl:
    """ Tests for the phish_ai_scan_url function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("artifact_value, expected_results", [
        ("https://google.com", {}),
        ("https://startup417.gb.net/M3?mes1=asdf@asdf.com", {})
    ])
    def test_success(self, circuits_app, artifact_value, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "artifact_value": artifact_value
        }
        results = call_phish_ai_scan_url_function(circuits_app, function_params)
        assert artifact_value == results["content"]["url"]
        assert "scan_id" in results["content"]
