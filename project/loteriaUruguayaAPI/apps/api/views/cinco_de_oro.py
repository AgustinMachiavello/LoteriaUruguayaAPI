"""Cinco de oro views"""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from ..models.games import Game

# Serializers
from ..serializers.games import GameModelSerializer

# Permissions
from rest_framework.permissions import (
	IsAuthenticated,
	IsAdminUser,
	AllowAny,
)

# FIXME TESTING
from ..periodic_tasks.update_cinco_de_oro_results import (
	extract_results_cinco_de_oro_2,
	create_cinco_de_oro_prize,
)


class CincoDeOroViewSet(
	mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	viewsets.GenericViewSet,
	mixins.ListModelMixin):

	"""
	Cinco de oro view set

	Hanlde update of results
	"""

	queryset = Game.objects.all()
	serializer_class = GameModelSerializer
	lookup_field = 'game_id'

	def get_permissions(self):
		"""Assign permissions based on action."""
		if self.action in ['udpate_results']:
			permissions = [AllowAny, ]
		else:
			permissions = [AllowAny, ]
		return [p() for p in permissions]

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = GameModelSerializer(instance=instance)
		return Response(serializer.data)

	def create(self, request, *args, **kwargs):
		serializer = ClientCreationModelSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)

	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = GameModelSerializer(
			instance=instance,
			data=request.data
		)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)

	def partial_update(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = GameModelSerializer(
			instance=instance,
			data=request.data,
			partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)

	@action(detail=False, methods=['get'])
	def update_results(self, request):
		"""Fetches results and creates a new instance of cinco de oro result"""
		results = extract_results_cinco_de_oro_2()
		prize = create_cinco_de_oro_prize(results[0])
		data = {
			'results': str(prize),
		}
		return Response(data, status=status.HTTP_201_CREATED)