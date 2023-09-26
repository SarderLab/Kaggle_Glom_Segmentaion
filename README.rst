================================================
PTC segmentation
================================================

PTC Segmentation is a DigitalSlideArchive plugin developed to segment PTC compartments from Kidney Whole Slide Images

How to use the Plugin
----------------------

**1- Open Digital Slide Archive**

  Launch the Digital Slide Archive platform.

**2- Select the Kidney Whole slide image for segmentation**

  Locate and choose / Upload the specific kidney whole slide image that you wish to segment using the PTC Segmentation plugin.

**3- Open HistomicsUI**

  Access the HistomicsUI, the user interface for the PTC Segmentation plugin.

**4- Click on Analyses and select PTC Segmentation**

  Inside HistomicsUI, navigate to the "Analyses" section, and then choose "PTC Segmentation" from the available options.

.. image:: https://github.com/SarderLab/PTC_segmentation/blob/praveen-ptc/ptc/Images/select%20plugin.png
  :width: 100%
  :alt: Selecting the PTC Segmentation Plugin

**5- Select the Base Directory**

  Specify the base directory, which should be the folder containing the kidney whole slide image you selected for segmentation.

**6- Select the model for PTC Segmentation**

  Pick the appropriate model for the PTC segmentation. This model will be used to perform the segmentation analysis.

.. image:: https://github.com/SarderLab/PTC_segmentation/blob/praveen-ptc/ptc/Images/directory%20and%20model.png
  :width: 100%
  :alt: Inputs for Segmentation

**7- Accessing Annotations**

  If you wish to view the annotations generated after the segmentation process or access the results of previous segmentations, return to the Digital Slide Archive. Under the specific image, you can find the "Annotations" section, where you can access the relevant information.


Building and Importing the Plugin as a Docker Image
---------------------------------------------------

The easiest way to use this code is to build it as a docker image which can be imported into the `Digital Slide Archive`_ as plugins:

  *To Build the docker image*::

    In the directory containing Dockerfile
    
      $ docker build -t <username>/<docker imagename>:<tag> .

    **Importing to AWS DSA instance:**

      $ docker push <username>/<docker imagename>:<tag>

    **Importing to Athena:**

      Create a Dockerfile and copy-paste the code below
  
        $ FROM <username>/<docker imagename>:<tag>
        $ ARG DSA_USER=1001
  
        $ USER ${DSA_USER}
    
      Move to the directory with the new Dockerfile and run the following
  
        $ docker build -t <username>/<docker imagename>:<new-tag> .
        $ docker push <username>/<docker imagename>:<new-tag>
  

  This image can be imported to a running version of the `Digital Slide Archive`_ under <Admin console / Plugins / Slicer CLI Web (gear icon)>


A video overview of the plugin is available `here <>`__

Refer to the `DSA website`_ for more information.


See Also
---------

**DSA/HistomicsTK project website:**
`Demos <https://digitalslidearchive.github.io/digital_slide_archive/demos-examples/>`_ |
`Success stories <https://digitalslidearchive.github.io/digital_slide_archive/success-stories/>`_

**Source repositories:** `Digital Slide Archive`_ | `HistomicsUI`_ | `large_image`_ | `slicer_cli_web`_

.. Links for everything above (not rendered):
.. _Brendon Lutnick: https://github.com/brendonlutnick
.. _HistomicsTK: https://github.com/DigitalSlideArchive/HistomicsTK
.. _DeepLab: https://github.com/tensorflow/models/tree/master/research/deeplab
.. _DeepLab codebase: https://github.com/SarderLab/HistomicsTK-deeplab/tree/main/histomicstk/deeplab
.. _Digital Slide Archive: http://github.com/DigitalSlideArchive/digital_slide_archive
.. _HistomicsUI: http://github.com/DigitalSlideArchive/HistomicsUI
.. _large_image: https://github.com/girder/large_image
.. _DSA website: https://digitalslidearchive.github.io/digital_slide_archive/
.. _slicer execution model: https://www.slicer.org/slicerWiki/index.php/Slicer3:Execution_Model_Documentation
.. _slicer_cli_web: https://github.com/girder/slicer_cli_web
.. _Docker: https://www.docker.com/
.. _Kitware: http://www.kitware.com/
