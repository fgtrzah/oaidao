from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FineTuneHyperparams")


@_attrs_define
class FineTuneHyperparams:
    """The hyperparameters used for the fine-tuning job. See the [fine-tuning guide](/docs/guides/legacy-fine-
    tuning/hyperparameters) for more details.

        Attributes:
            batch_size (int): The batch size to use for training. The batch size is the number of
                training examples used to train a single forward and backward pass.
            learning_rate_multiplier (float): The learning rate multiplier to use for training.
            n_epochs (int): The number of epochs to train the model for. An epoch refers to one
                full cycle through the training dataset.
            prompt_loss_weight (float): The weight to use for loss on the prompt tokens.
            classification_n_classes (Union[Unset, int]): The number of classes to use for computing classification metrics.
            classification_positive_class (Union[Unset, str]): The positive class to use for computing classification
                metrics.
            compute_classification_metrics (Union[Unset, bool]): The classification metrics to compute using the validation
                dataset at the end of every epoch.
    """

    batch_size: int
    learning_rate_multiplier: float
    n_epochs: int
    prompt_loss_weight: float
    classification_n_classes: Union[Unset, int] = UNSET
    classification_positive_class: Union[Unset, str] = UNSET
    compute_classification_metrics: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batch_size = self.batch_size
        learning_rate_multiplier = self.learning_rate_multiplier
        n_epochs = self.n_epochs
        prompt_loss_weight = self.prompt_loss_weight
        classification_n_classes = self.classification_n_classes
        classification_positive_class = self.classification_positive_class
        compute_classification_metrics = self.compute_classification_metrics

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batch_size": batch_size,
                "learning_rate_multiplier": learning_rate_multiplier,
                "n_epochs": n_epochs,
                "prompt_loss_weight": prompt_loss_weight,
            }
        )
        if classification_n_classes is not UNSET:
            field_dict["classification_n_classes"] = classification_n_classes
        if classification_positive_class is not UNSET:
            field_dict["classification_positive_class"] = classification_positive_class
        if compute_classification_metrics is not UNSET:
            field_dict["compute_classification_metrics"] = compute_classification_metrics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        batch_size = d.pop("batch_size")

        learning_rate_multiplier = d.pop("learning_rate_multiplier")

        n_epochs = d.pop("n_epochs")

        prompt_loss_weight = d.pop("prompt_loss_weight")

        classification_n_classes = d.pop("classification_n_classes", UNSET)

        classification_positive_class = d.pop("classification_positive_class", UNSET)

        compute_classification_metrics = d.pop("compute_classification_metrics", UNSET)

        fine_tune_hyperparams = cls(
            batch_size=batch_size,
            learning_rate_multiplier=learning_rate_multiplier,
            n_epochs=n_epochs,
            prompt_loss_weight=prompt_loss_weight,
            classification_n_classes=classification_n_classes,
            classification_positive_class=classification_positive_class,
            compute_classification_metrics=compute_classification_metrics,
        )

        fine_tune_hyperparams.additional_properties = d
        return fine_tune_hyperparams

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
