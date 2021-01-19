"""
Configurations of the Website subpages from the App: video-content
"""

from django.shortcuts import render
# pylint: disable = import-error,relative-beyond-top-level
from .models import Video
from details_page.models import Era


def display(request):
    """
    Subpage to show all videos sorted into fitting era
    :param request: url request to get subpage /videos
    :return: rendering the subpage based on videos.html
    with a context variable to get Videos sorted in eras
    """

    context = {
        'Frühzeit': Video.get_era(Video, 'Frühzeit'),
        'Archaik': Video.get_era(Video, 'Archaik'),
        'Klassik': Video.get_era(Video, 'Klassik'),
        'Hellenismus': Video.get_era(Video, 'Hellenismus'),
        'RömischeKaiserzeit': Video.get_era(Video, 'Römische Kaiserzeit'),
        'Spätantike': Video.get_era(Video, 'Spätantike'),

        'Era': (Video.get_era(Video, 'Frühzeit'),
                Video.get_era(Video, 'Archaik'),
                Video.get_era(Video, 'Klassik'),
                Video.get_era(Video, 'Hellenismus'),
                Video.get_era(Video, 'Römische Kaiserzeit'),
                Video.get_era(Video, 'Spätantike')),

        'Test': {"1": [1,2,3,4], "2": [5,6,7,8]}
    }

    return render(request, 'videos.html', context)

    """
    def getYearOfItemAsSignedInt(era):
    
    
        Inner helper to sorting the years.
        :param era: the era to get the year from
        :return: the year of the era (beginning year)
      
      
        try:
            if era.year_from_BC_or_AD == "v.Chr.":
                return -1 * int(era.year_from)
            else:
                return int(era.year_from)
        except TypeError:
            # If era has no year return 2021, so it will be listed last.
            return 2021

    eras = Era.objects.filter(visible_on_video_page=True)
    eras = sorted(eras, key=lambda era: getYearOfItemAsSignedInt(era))
    context = {}
    for e in eras:
        context[e.name] = Video.get_era(Video, e.pk)
    """
