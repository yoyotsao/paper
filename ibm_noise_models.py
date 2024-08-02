# ibm_noise_models.py

from qiskit_aer.noise import NoiseModel, depolarizing_error, thermal_relaxation_error
from qiskit_aer.noise import amplitude_damping_error, phase_damping_error
import numpy as np

def combined_noise_backend_normdist(num_qubits):
    """
    Create a combined noise model with normal distribution noise.

    Args:
        num_qubits (int): Number of qubits in the noise model.

    Returns:
        NoiseModel: A Qiskit NoiseModel instance with combined noise.
    """
    # Create a noise model instance
    noise_model = NoiseModel()

    # Example parameters (you may need to adjust these based on your requirements)
    depolarizing_prob = 0.01
    amplitude_damping_param = 0.05
    phase_damping_param = 0.1
    t1 = 100  # Relaxation time
    t2 = 100  # Dephasing time

    # Create noise errors
    depolarizing = depolarizing_error(depolarizing_prob, num_qubits)
    amplitude_damping = amplitude_damping_error(amplitude_damping_param)
    phase_damping = phase_damping_error(phase_damping_param)
    thermal_relaxation = thermal_relaxation_error(t1=t1, t2=t2, gate_time=1.0)

    # Add noise errors to the model
    noise_model.add_all_qubit_quantum_error(depolarizing, ['u1', 'u2', 'u3', 'cx'])
    noise_model.add_all_qubit_quantum_error(amplitude_damping, ['u1', 'u2', 'u3', 'cx'])
    noise_model.add_all_qubit_quantum_error(phase_damping, ['u1', 'u2', 'u3', 'cx'])
    noise_model.add_all_qubit_quantum_error(thermal_relaxation, ['u1', 'u2', 'u3', 'cx'])

    return noise_model
