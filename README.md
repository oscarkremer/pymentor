# Pymentor

Mentor is a Python library to implement a computational model of the Mentor Didactic Robotic Arm. This model was first published in the work *A Genetic Approach for Trajectory Optimization Applied to a Didactic Robot*. The library includes:

* Direct kinematics based on Denavit-Hartenberg parameters, where variables represented in the cartesian coordinate space are transformed to joint space.
* Inverse kinematics to encounter joint angles based on position and orientation matrix.
* Exception and error treatment in case of impossible position/orientation pairs.
* Method to deal with alpha, beta and gamma angles to encounter orientation 3x3 matrix based on XYZ angles.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pymentor.

```bash
pip install pymentor
```

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.


```python
import pymentor

```

## Contributing

Any contributions you make are **greatly appreciated**. To contribute please follow this steps:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/new_feature`)
3. Commit your Changes (`git commit -m 'commit-tag: commit-description'`)
4. Push to the Branch (`git push origin feature/new_feature`)
5. Open a Pull Request

## License
General Public License version 3.0 [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)

## Contact

Oscar Schmitt Kremer - [Linkedin](https://www.linkedin.com/in/oscar-kremer/) [Email](oscar.s.kremer@hotmail.com)

Project Link: [pymentor Repository](https://github.com/oscarkremer/pymentor)

## References

O. S. Kremer, M. A. B. Cunha, F. S. Moraes, S. S. Schiavon. *A Genetic Apporach for Trajectory Optimization Applied to a Didactic Robot* **2019 Latin American Robotics Symposium**. 2019.
[doi:10.1109/LARS-SBR-WRE48964.2019.00049](doi:10.1109/LARS-SBR-WRE48964.2019.00049)