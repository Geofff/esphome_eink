from esphome import core, pins
import esphome.codegen as cg
from esphome.components import display, spi
import esphome.config_validation as cv
from esphome.const import (
    CONF_BUSY_PIN,
    CONF_DC_PIN,
    CONF_FULL_UPDATE_EVERY,
    CONF_ID, 
    CONF_LAMBDA,
    CONF_MODEL,
    CONF_PAGES,
    CONF_RESET_DURATION,
    CONF_RESET_PIN,
    CONF_ROTATION,
)

DEPENDENCIES = ["spi"]

gc_eink_ns = cg.esphome_ns.namespace("gc_eink")
EPaper7P5In_P = gc_eink_ns.class_("EPaper7P5In_P", display.Display, cg.PollingComponent)

CONFIG_SCHEMA = cv.All(
    display.FULL_DISPLAY_SCHEMA.extend(
        {
            cv.GenerateID(): cv.declare_id(EPaper7P5In_P),
            cv.Required(CONF_DC_PIN): pins.gpio_output_pin_schema,
            cv.Required(CONF_MODEL): cv.one_of("epaper7p5in_p", lower=True),
            cv.Optional(CONF_RESET_PIN): pins.gpio_output_pin_schema,
            cv.Optional(CONF_BUSY_PIN): pins.gpio_input_pin_schema,
            cv.Optional(CONF_FULL_UPDATE_EVERY): cv.positive_int,
            cv.Optional(CONF_RESET_DURATION): cv.positive_time_period_milliseconds,
        }
    )
    .extend(cv.polling_component_schema("5s"))
    .extend(spi.spi_device_schema()),
    cv.has_at_most_one_key(CONF_PAGES, CONF_LAMBDA),
)

FINAL_VALIDATE_SCHEMA = spi.final_validate_device_schema(
    "gc_eink",
    require_miso=False,
    require_mosi=True
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await display.register_display(var, config)
    await spi.register_spi_device(var, config)

    if CONF_DC_PIN in config:
        dc = await cg.gpio_pin_expression(config[CONF_DC_PIN])
        cg.add(var.set_dc_pin(dc))

    if CONF_RESET_PIN in config:
        reset = await cg.gpio_pin_expression(config[CONF_RESET_PIN])
        cg.add(var.set_reset_pin(reset))

    if CONF_BUSY_PIN in config:
        busy = await cg.gpio_pin_expression(config[CONF_BUSY_PIN])
        cg.add(var.set_busy_pin(busy))
        
    if CONF_ROTATION in config:
        cg.add(var.set_rotation(config[CONF_ROTATION]))

    if CONF_FULL_UPDATE_EVERY in config:
        cg.add(var.set_full_update_every(config[CONF_FULL_UPDATE_EVERY]))

    if CONF_RESET_DURATION in config:
        cg.add(var.set_reset_duration(config[CONF_RESET_DURATION]))

    if CONF_LAMBDA in config:
        lambda_ = await cg.process_lambda(
            config[CONF_LAMBDA], [(display.DisplayRef, "it")], return_type=cg.void
        )
        cg.add(var.set_writer(lambda_))
